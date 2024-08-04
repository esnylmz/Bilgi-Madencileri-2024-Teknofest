from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import re
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd
import json

app = FastAPI()

# Load the fine-tuned sentiment model and tokenizer
model_path = 'C:/Users/Onur/Downloads/fine-tuned-model'
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

# Check if GPU is available and set the device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Initialize the sentiment analysis pipeline with the fine-tuned model
sentiment_model = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer, device=0 if device.type == 'cuda' else -1)

# NER model loading
ner_model = pipeline("ner", model="savasy/bert-base-turkish-ner-cased", device=0 if device.type == 'cuda' else -1)

def combine_subwords(entities):
    combined_entities = []
    current_entity = ""

    for entity in entities:
        if entity['entity'].startswith('B-') or entity['entity'].startswith('I-'):
            if entity['entity'] in ['B-ORG', 'I-ORG']:
                if entity['word'].startswith('##'):
                    current_entity += entity['word'].replace('##', '')
                else:
                    if current_entity:
                        combined_entities.append(current_entity)
                        current_entity = ""
                    current_entity = entity['word']

    if current_entity:
        combined_entities.append(current_entity)

    combined_entities = list(set(combined_entities))

    return combined_entities

def analyze_entity_sentiment(text, entities):
    results = []
    sentences = re.split(r'(?<=[.!?]) +', text)  # Split text into sentences
    for entity in entities:
        for sentence in sentences:
            if entity in sentence:
                sentiment = sentiment_model(sentence)
                results.append({
                    "entity": entity,
                    "sentiment": sentiment[0]['label'],
                    "sentence": sentence
                })
                break  # Move to the next entity after finding the relevant sentence
    return results

def analyze_text(text):
    # Entity extraction
    entities = ner_model(text)

    # Combine subword tokens and filter for ORGANISATION entities
    combined_entities = combine_subwords(entities)

    # Analyze sentiment for each entity
    results = analyze_entity_sentiment(text, combined_entities)

    return results

def format_analysis(text, analysis):
    entity_list = list(set([item['entity'] for item in analysis if len(item['entity']) > 2]))
    results = [{'entity': item['entity'], 'sentiment': item['sentiment'], 'sentence': item['sentence']} for item in analysis if len(item['entity']) > 2]
    return {
        'text': text,
        'results': results
    }

class TextRequest(BaseModel):
    text: str

@app.post("/analyze/")
async def analyze_text_endpoint(request: TextRequest):
    text = request.text
    try:
        analysis = analyze_text(text)
        result = format_analysis(text, analysis)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
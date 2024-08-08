@echo off
REM Change directory to where your server.py is located
cd /d "C:\path\to\your\directory"

REM Activate your virtual environment if you have one
REM Example for virtualenv on Windows:
REM call venv\Scripts\activate

REM Run uvicorn with the server.py file
uvicorn server:app --reload

REM Pause the command prompt to see any messages
pause

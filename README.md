# BİLGİ MADENCİLERİ TAKIMI, 2024 TEKNOFEST
TEKNOFEST 2024 TÜRKÇE DOĞAL DİL İŞLEME SENARYOSU

![image](https://github.com/esnylmz/Bilgi-Madencileri-2024-Teknofest/assets/102979440/c0e732f8-7cc1-46a9-b57f-ba6d28987075)

# TAKIMIMIZ HAKKINDA: 
Takımımız 2024 yılında İstanbul Bilgi Üniversitesi Bilgisayar Mühendisliği son sınıf öğrencisi olan Emine Esin Yılmaz, Ege Eylül Kırmızı ve Onur Çalışkan tarafından kurulmuştur. Takımımız 2024 yılı Türkçe Doğal Dil işleme Yarışmasına Senaryo kategorisinde katılmaya hak kazanmıştır.Takımımız geliştirilen proje ile sektör ile işbirliği içerisinde, verilerin Türkçe dil modelleri ile analizini, verilerin işlenerek sektöre fayda sağlayacak sonuçların ve model geliştirmelerinin elde edilmesini amaçlamaktadır. 

## Takım Üyeleri:
- Emine Esin YILMAZ-İstanbul Bilgi Üniversitesi-Bilgisayar Mühendisliği: Takım Kaptanı, Developer
- Ege Eylül Kırmızı-İstanbul Bilgi Üniversitesi-Bilgisayar Mühendisliği : Developer
- Onur Çalışkan-İstanbul Bilgi Üniversitesi-Bilgisayar Mühendisliği : Backend Developer

# PROJE VE METODOLOJİ

## Projemizin Amacı ve Katkı Değeri
Projemiz, Teknofest 2024 Türkçe Doğal Dil İşleme Senaryosu hedeflerine paralel olarak, Turkcell şirketi ve hizmetleri hakkında kullanıcıların yorumlarının incelenmesi, bu yorumlardan varlık çıkarımı yapılması ve varlıkların cümle içindeki bağlamını da göz önüne alarak genel duygusunu belirleme üzerine odaklanmıştır.

Projemizde Türkçe sentiment modellerinin sektörün ihtiyacına göre labellar eklenerek fine-tune edilmesi ve iyileştirilmesi üzerine yoğunlaşılmıştır. 
Turkcell veri seti özelinde yorumları elde edebilmek için duygu durumunda kullanılan negatif eitketi 2 sınıfa ayrılmıştır:

- Negative - Service Issues  (Olumsuz - Hizmet ve Servis ile İlgili Sorunlar)
- Negative - Pricing and Package Issues (Olumsuz - Fiyatlandırma ve Paket ile İlgili Sorunlar)

  Negatif etiketinin yukarıda belirtilen iki sınıfa ayrılması ile modelimizi kullanan kullanıcıların ürünlerini daha detaylı bir şekilde analiz etme ve farklı kategorileri kendi içinde değerlendirebilme imkanının geliştirilmesi üzerinde çalışma yapılmıştır.

## Veri Setinin Hazırlanması

- Projenin ilk adımında BeautifulSoup kütüphanesi kullanılarak web-kazıma yöntemi ile sikayetvar.com sitesinden Turkcell başlığı altında olan kullanıcı yorumları çekilmiştir.
- Web kazıma yönetmi ile çekilen yorum verisinin bir kısmı etiketlenmek için ayrılmıştır
- Verinin çeşitlendirilmesini sağlamak amacıyla web-kazıma ile elde edilen şikayetvar yorumlarının yanı sıra Turkcell Twitter Veriseti'nden yaklaşık 500 veri de verisetine eklenmiştir.

## Özellik Çıkarımı ve Sentiment (Duygu) Analizi Modellerinin Kullanımı ve Geliştirilmesi
- Özellik çıkarımı için pre-trained bir model olan savasy/bert-base-turkish-ner-cased modeli kullanılmıştır. Model sonucu etiketlenen veride Organisation (Organizasyon) etiketli olan kelimeler filtrelenmiş, B-ORG ve I-ORG kelimeleri incelenmiş ve kelimelerin doğru bir şekilde birleştirilmesi için B-ORG ve I-ORG etiketli yarım kelimeleri birleştiren bir düzenleme fonksiyonu kod içine eklenmiştir. Bu fonksiyon ile NER sonucu elde edilen kelimelerin doğruluğu artırılmıştır ve yarım kalan kelime öbekleri elimine edilmiştir.
- Sentiment (Duygu Analizi) için pre-trained bir model olan savasy/bert-base-turkish-sentiment-cased modeli fine-tune edilmiştir. Orijinalinde Negative ve Positive olmak üzere iki etikete sahip olan bu model, sektörün ihtiyacı göz önünde bulunarak etiketlerin çeşitlendirilmesi ve yorumun kolaylaştırılması için farklı etiketler üzerinde eğitilerek fine-tune edilmiştir. Fine-tune sonucu projemizde duygu analizinde kullanılan 4 etiket bulunmaktadır:
- Positive
- Neutral
- Negative - Service Issues
- Negative - Pricing and Package Issues
Modelin fine-tune edilmesi için web kazıma ve Twitter Turkcell verilerinin birleştirilmesi ile elde edilen veriseti takmımız tarafından eğitim için etiketlenmiştir.

Projemizde Negatif yorum sınıfını 2 kategoriye ayırarak sektörün ihtiyaçlarına yönelik bir model oluşturulması amaçlanmıştır. Var olan modeller ve veri seti incelendiğinde modellerin veri setinde bulunan yorumların analizini tam olarak karşılayacak etiketlere sahip olmadığı tespit edilmiş ve projemiz bu durumun iyileştirilmesine yönelik bir çalışma yürütmüştür.

# Proje Sonuçları

Projede fine-tune edilen savasy/bert-base-turkish-sentiment-cased duygu analizi modeli, etiketlenen yeni veriler ile 3 epoch sonucunda 0.89 accuracy (doğruluk) elde etmiştir. 
İki modelin birleştirilmesi ve web-servisinin ayağa kaldırılması sonucunda modelin elde ettiği sonuçlar aşağıdaki gibidir:


# MODELİN ÇALIŞTIRILMASI

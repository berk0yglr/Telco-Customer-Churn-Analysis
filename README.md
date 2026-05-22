# 📊 Müşteri Terk (Churn) Analizi ve Korelasyon İncelemesi

Bu proje, bir telekomünikasyon şirketinin müşteri verilerini kullanarak, hangi özelliklerin müşterilerin aboneliklerini iptal etmesine (Churn) yol açtığını istatistiksel olarak analiz eden bir veri bilimi çalışmasıdır. Veri temizleme, dönüştürme ve görselleştirme süreçleri uçtan uca uygulanmıştır.

## 🎯 Projenin Amacı
Şirketlerin en büyük maliyetlerinden biri mevcut müşteriyi kaybetmektir. Bu projedeki Python betiği;
* Ham müşteri verisini alır ve eksik/hatalı verileri (Data Anomalies) temizler.
* Kategorik verileri makine öğrenmesine hazır hale getirmek için 1 ve 0'lara (One-Hot Encoding) çevirir.
* Churn (Terk) durumu ile diğer tüm müşteri özellikleri arasındaki **Korelasyon (İlişki) Skorlarını** hesaplar.
* Sonuçları yöneticilerin veya pazarlama ekiplerinin anlayabileceği şekilde ısı haritası mantığıyla çubuk grafiğe (Barplot) döker.

## 🛠️ Kullanılan Teknolojiler
* **Python** (Veri işleme ve mantık)
* **Pandas & NumPy** (Veri manipülasyonu, temizliği ve korelasyon matrisi)
* **Matplotlib & Seaborn** (Veri görselleştirme)

## 📁 Veri Seti (Önemli Not)
> KVKK ve veri güvenliği standartları (Best-Practices) gereği, projede kullanılan veri seti bu repoya **yüklenmemiştir.**

Proje, Kaggle üzerinde bulunan anonimleştirilmiş açık kaynaklı veri seti ile geliştirilmiştir:
🔗 **[Kaggle - Telco Customer Churn Veri Seti](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)**

Kodu kendi bilgisayarınızda çalıştırmak için yukarıdaki linkten veriyi indirip, adını `churn_verisi.csv` olarak değiştirerek proje ana dizinine eklemeniz yeterlidir.

## 🚀 Projeyi Çalıştırma

1. Repoyu bilgisayarınıza klonlayın:
   ```bash
   git clone [https://github.com/](https://github.com/)<KULLANICI_ADIN>/<REPO_ADIN>.git
2.Gerekli kütüphaneleri kurun: pip install -r requirements.txt
3.Veri setini ana dizine ekledikten sonra analizi başlatın:python main.py

Yapılan korelasyon analizi sonucunda elde edilen veriler şu şekildedir:

Müşteriyi En Çok Kaçıran Etkenler (+1'e yakın): Fiber optik internet altyapısındaki sorunlar, manuel (elektronik çek) ödeme yöntemleri ve yüksek aylık fatura tutarları.

Müşteriyi İçeride Tutan Etkenler (-1'e yakın): Uzun süreli müşterilik (tenure) ve 2 yıllık taahhütlü sözleşmeler.

(Grafiğin görseli aşağıdadır)
<img width="1183" height="823" alt="image" src="https://github.com/user-attachments/assets/51b2bc5a-c6de-41b4-895e-b493a12cbf40" />



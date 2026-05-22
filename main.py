import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("churn_verisi.csv")

df.drop('customerID', axis=1, inplace=True)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
df.dropna(inplace=True)

df_encoded = pd.get_dummies(df, drop_first=True)

korelasyon = df_encoded.corr()['Churn'].sort_values(ascending=False)
korelasyon_grafik = korelasyon.drop('Churn')

turkce_isimler = {
    'InternetService_Fiber optic': 'Fiber Optik İnternet',
    'PaymentMethod_Electronic check': 'Elektronik Çek Ödemesi',
    'MonthlyCharges': 'Aylık Fatura Tutarı',
    'PaperlessBilling_Yes': 'Dijital Fatura',
    'SeniorCitizen': '65+ Yaş Müşteri',
    'StreamingTV_Yes': 'TV Yayını Alıyor',
    'StreamingMovies_Yes': 'Film Yayını Alıyor',
    'MultipleLines_Yes': 'Çoklu Telefon Hattı',
    'PhoneService_Yes': 'Telefon Hizmeti Var',
    'gender_Male': 'Cinsiyet: Erkek',
    'MultipleLines_No phone service': 'Telefon Hizmeti Yok',
    'DeviceProtection_Yes': 'Cihaz Koruması Var',
    'OnlineBackup_Yes': 'Bulut Yedekleme Var',
    'PaymentMethod_Mailed check': 'Posta Çeki Ödemesi',
    'PaymentMethod_Credit card (automatic)': 'Kredi Kartı (Otomatik)',
    'Partner_Yes': 'Evli / Partneri Var',
    'Dependents_Yes': 'Bakmakla Yükümlü Kişi Var',
    'TechSupport_Yes': 'Teknik Destek Alıyor',
    'OnlineSecurity_Yes': 'Online Güvenlik Paketi',
    'Contract_One year': '1 Yıllık Sözleşme',
    'TotalCharges': 'Toplam Ödenen Tutar',
    'InternetService_No': 'İnternet Kullanmıyor',
    'StreamingTV_No internet service': 'TV (İnternetsiz)',
    'OnlineSecurity_No internet service': 'Güvenlik (İnternetsiz)',
    'OnlineBackup_No internet service': 'Yedekleme (İnternetsiz)',
    'DeviceProtection_No internet service': 'Cihaz Koruma (İnternetsiz)',
    'StreamingMovies_No internet service': 'Film (İnternetsiz)',
    'TechSupport_No internet service': 'Teknik Destek (İnternetsiz)',
    'Contract_Two year': '2 Yıllık Sözleşme',
    'tenure': 'Müşterilik Süresi (Ay)'
}

korelasyon_grafik = korelasyon_grafik.rename(index=turkce_isimler)

plt.figure(figsize=(12, 8))
sns.barplot(x=korelasyon_grafik.values, y=korelasyon_grafik.index, hue=korelasyon_grafik.index, palette="coolwarm", legend=False)

plt.title('Müşterileri Ne Kaçırıyor, Ne Tutuyor? (Churn Korelasyon Analizi)', fontsize=16, fontweight='bold')
plt.xlabel('Korelasyon Skoru (-1: Müşteriyi Tutar, +1: Müşteriyi Kaçırır)', fontsize=12)
plt.ylabel('Müşteri Özellikleri', fontsize=12)
plt.tight_layout()
plt.show()
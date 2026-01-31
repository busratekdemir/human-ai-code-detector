# 🤖 Human vs AI Code Detection System

Bu proje, yazılım kaynak kodlarının **insan tarafından mı yoksa yapay zekâ (AI) tarafından mı üretildiğini**
makine öğrenmesi yöntemleriyle tespit etmeyi amaçlayan bir **sınıflandırma sistemi**dir.

Farklı kaynaklardan (**GitHub API, GPT-4 vb.**) toplanan veri setleri üzerinde eğitilen modeller,
bir kullanıcı arayüzü üzerinden **gerçek zamanlı tahminler** yapabilmektedir.
Bu proje Python tabanlıdır ve yalnızca Python ekosistemi üzerinde çalışacak şekilde tasarlanmıştır.

---

## 🎯 Projenin Amacı

- **Ayırt Etme:** İnsan yazımı kodlar ile yapay zekâ çıktıları arasındaki yapısal farkları belirlemek  
- **Feature Extraction:** Kod metinlerinden anlamlı öznitelikler çıkararak metin madenciliği yapmak  
- **Model Karşılaştırma:** Farklı sınıflandırma algoritmalarının kod tespiti üzerindeki performansını analiz etmek  
- **Gerçek Zamanlı Kullanım:** Eğitilen modelleri son kullanıcı için bir arayüz ile erişilebilir kılmak  

---

## 🧠 Kullanılan Teknolojiler

Proje geliştirme sürecinde aşağıdaki kütüphane ve araçlar kullanılmıştır:

| Teknoloji | Kullanım Amacı |
|---------|---------------|
| Python | Ana programlama dili |
| Scikit-learn | Makine öğrenmesi modelleri ve veri ön işleme |
| Pandas & NumPy | Veri yönetimi ve analiz |
| Flask | Web tabanlı kullanıcı arayüzü |
| Pickle | Modellerin kaydedilmesi ve yüklenmesi (.pkl) |
| Jupyter Notebook | Eğitim ve veri çekme süreçleri |

---

## 📁 Proje Yapısı

```bash
human_ai/
├── data/                         # İnsan ve AI kod örneklerini içeren veri seti
├── Github Veri cekme.ipynb       # GitHub üzerinden veri toplama betiği
├── AI kod olusturma.ipynb        # AI (LLM) kullanarak veri seti üretimi
├── Egitim.ipynb                 # Veri ön işleme, vektörleştirme ve eğitim
├── vectorizer.pkl               # Metinleri sayısal verilere dönüştüren araç
├── DecisionTreeClassifier.pkl   # Karar Ağacı modeli
├── LogisticRegression.pkl       # Lojistik Regresyon modeli
├── RandomForestClassifier.pkl   # Rastgele Orman modeli
```

⚙️ Çalışma Mantığı

Proje genel olarak **5 ana aşamadan** oluşmaktadır:

1. **Veri Toplama**  
   GitHub API kullanılarak farklı geliştiricilerin kodları çekilir ve AI araçlarıyla benzer kodlar ürettirilir.

2. **Etiketleme**  
   Toplanan kodlar **Human** ve **AI** olarak sınıflandırılır.

3. **Vektörleştirme**  
   Kod blokları, makine öğrenmesi modellerinin anlayabileceği sayısal vektörlere dönüştürülür.

4. **Eğitim**  
   Random Forest, Logistic Regression ve Decision Tree algoritmalarıyla modeller eğitilir.

5. **Tahmin**  
   En başarılı modeller `.pkl` formatında kaydedilerek kullanıcı arayüzüne entegre edilir.

---

## 🧪 Kullanılan Modeller

Eğitim sürecinde aşağıdaki modeller kullanılmış ve başarı oranları karşılaştırılmıştır:

- **Decision Tree Classifier**
- **Logistic Regression**
- **Random Forest Classifier**  
  - *(Genellikle en yüksek doğruluk oranını sağlamıştır)*

---

## ▶️ Uygulamayı Çalıştırma

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyiniz:

1️⃣ Gerekli Kütüphaneleri Yükleyin

pip install pandas numpy scikit-learn flask

2️⃣ Uygulamayı Başlatın
python app_ui.py

3️⃣ Tarayıcıdan Erişin
http://127.0.0.1:5000


Analiz etmek istediğiniz kodu arayüz üzerinden girerek sonucu görüntüleyebilirsiniz.

👩‍💻 Proje Ekibi

Bu proje Manisa Celal Bayar Üniversitesi – Yazılım Mühendisliği bölümü kapsamında geliştirilmiştir.

Büşra Tekdemir

Mehmet Utku Bala

Bayram Gülcan

İsmet Şen

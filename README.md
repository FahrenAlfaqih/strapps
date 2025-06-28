# 🧠 STRapps – Scene Text Recognition Web App

**STRapps** adalah aplikasi web berbasis Python dan Flask yang memungkinkan pengguna mengunggah gambar dan mendapatkan hasil ekstraksi teks secara otomatis menggunakan model deep learning STR (Scene Text Recognition). Model dilatih menggunakan arsitektur CRNN (CNN + BiLSTM + CTC) dan dapat mengenali kata dari gambar dunia nyata.

---

## 📦 Dataset – IIIT 5K-Word

Dataset yang digunakan adalah **IIIT 5K-Word**, benchmark populer untuk scene text recognition:

- 📸 Berisi 5.000+ gambar teks (satu kata per gambar)
- 🔤 Label disediakan dalam format string satu kata (word-level)
- 🧪 Training set: 2.000 gambar, Testing set: 3.000 gambar
- 🌍 Gambar dikumpulkan dari internet dan mencerminkan kondisi dunia nyata
- 📂 Format `.mat` dengan label dan nama file

🔗 [Download Dataset IIIT5K](http://cvit.iiit.ac.in/research/projects/cvit-projects/scene-text-recognition)

---

## 🔄 Data Preprocessing

Untuk meningkatkan generalisasi model, preprocessing gambar meliputi:

- Konversi ke grayscale
- Resize ke dimensi 32x128 piksel
- Normalisasi piksel ke format tensor
- Transformasi dimensi untuk input ke CNN → LSTM

---

## ⚙️ Fitur Aplikasi

- 📤 Upload gambar dengan UI stylish (Tailwind CSS)
- 🧠 Deteksi dan ekstraksi teks otomatis dari gambar menggunakan model STR
- 🌐 Web interface ringan (Flask + HTML + JS)
- 🎯 Model inference akurat dan cepat
- 🖼️ Tampilkan hasil prediksi teks secara langsung
- 🚀 Siap deploy ke server publik / cloud

---

## 🧪 Performa Model

Model dilatih selama 30 epoch dengan loss menurun dari **4.28 → 0.10**. Evaluasi akurasi menggunakan pengujian string-level menunjukkan performa tinggi pada test set IIIT5K.

> Model: `SimpleSTR`  
> Arsitektur: CNN → BiLSTM → FC + CTC Loss  
> Evaluasi: String-level accuracy via CTC decoding

---

## 🚀 Cara Menjalankan Aplikasi

```bash
# 1. Clone repo
git clone https://github.com/FahrenAlfaqih/strapps.git
cd strapps

# 2. Install dependency
pip install flask flask-cors torch torchvision

# 3. Jalankan server Flask
python app.py

# 4. Buka frontend HTML di browser
http://localhost/strapps/index.html
```

## 📁 Struktur Folder 
Strapps/
 │
 ├── App.py
 ├── index.html
 ├── model_str.path
 │
 └── README.md


## 🖼️ Tampilan Antarmuka
![image](https://github.com/user-attachments/assets/9196688a-6783-4d24-826a-b7db2ec5caf2)

## 🙋‍♂️ Kontributor
Dikembangkan oleh Fahren Alfaqih sebagai bagian dari proyek Computer Vision STR (Scene Text Recognition) berbasis web.

## 📄 Lisensi
MIT License © 2025 Fahren Alfaqih


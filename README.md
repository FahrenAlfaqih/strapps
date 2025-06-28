# 🧠 STRapps – Scene Text Recognition Web App

**STRapps** adalah aplikasi web berbasis Python & Flask yang memungkinkan pengguna untuk mengunggah gambar dan mendapatkan hasil teks dari model OCR berbasis deep learning (CRNN).

---

## ✨ Fitur

- 🖼️ Upload gambar dengan UI stylish berbasis Tailwind CSS
- 🧠 Deep learning OCR dengan model CNN + LSTM (CRNN)
- 🔍 Otomatis mendeteksi dan mengekstrak teks dari gambar
- 🚀 Siap dikembangkan ke versi API, mobile, atau cloud deployment

---

## 🖼️ Demo Tampilan

![image](https://github.com/user-attachments/assets/c5ef6ffe-8813-4338-9d8c-1592cc0ab04c)
![image](https://github.com/user-attachments/assets/abdb326e-6e68-4ce4-877e-358c03bc386a)



---

## 🚀 Teknologi yang Digunakan

| Stack      | Teknologi                        |
|------------|----------------------------------|
| Backend    | Python, Flask, Torch             |
| Frontend   | HTML, Tailwind CSS, JavaScript   |
| Model OCR  | CRNN (CNN + BiLSTM + CTC Loss)   |
| Library    | PIL, torchvision, flask-cors     |

---

## 🛠️ Cara Menjalankan

1. **Clone repo ini**

```bash
git clone https://github.com/FahrenAlfaqih/strapps.git
cd strapps
```

2. **Install dependency (Python 3.8+)**
```bash
pip install flask flask-cors torch torchvision
```

3. **Jalankan backend Flask**
```bash
python app.py
```
4. **Buka index.html di browser**
http://localhost/strapps/index.html

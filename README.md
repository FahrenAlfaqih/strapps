# 🧠 STRapps – Scene Text Recognition Web App

**STRapps** is a web-based application built with Python and Flask that enables users to upload an image and automatically extract text using a deep learning-based Scene Text Recognition (STR) model. The model is trained using the CRNN architecture (CNN + BiLSTM + CTC) and is capable of recognizing words from real-world images.

---

## 📦 Dataset – IIIT 5K-Word

This project uses the **IIIT 5K-Word** dataset, a popular benchmark for scene text recognition:

- 📸 Contains 5,000+ cropped word images (one word per image)
- 🔤 Labels are provided as word-level strings
- 🧪 Training set: 2,000 images; Testing set: 3,000 images
- 🌍 Images are collected from the internet and reflect real-world scenes
- 📂 Stored in `.mat` format with labels and image filenames

🔗 [Download IIIT5K Dataset](http://cvit.iiit.ac.in/research/projects/cvit-projects/scene-text-recognition)

---

## 🔄 Data Preprocessing

To enhance model generalization, each input image undergoes the following preprocessing steps:

- Convert to grayscale
- Resize to 32×128 pixels
- Normalize pixel values to tensor format
- Reshape dimensions to match input for CNN → LSTM

---

## ⚙️ Application Features

- 📤 Upload an image via a stylish Tailwind CSS-based UI
- 🧠 Automatically detect and extract text from uploaded images using the STR model
- 🌐 Lightweight web interface (Flask + HTML + JS)
- 🎯 Fast and accurate model inference
- 🖼️ Display prediction result instantly on screen
- 🚀 Ready for deployment to public servers or cloud environments

---

## 🧪 Model Performance

The model was trained for 30 epochs, with training loss decreasing from **4.28 → 0.10**. Accuracy evaluation using string-level comparison shows high performance on the IIIT5K test set.

> Model: `SimpleSTR`  
> Architecture: CNN → BiLSTM → FC + CTC Loss  
> Evaluation: String-level accuracy using CTC decoding

---

## 🚀 How to Run the Application

```bash
# 1. Clone the repository
git clone https://github.com/FahrenAlfaqih/strapps.git
cd strapps

# 2. Install dependencies
pip install flask flask-cors torch torchvision

# 3. Run Flask backend
python app.py

# 4. Open frontend in your browser
http://localhost/strapps/index.html
```

## 🖼️ Interfaces
### 📸 Image Test
![image](https://github.com/user-attachments/assets/bf826399-2a29-4beb-b533-453aff11c373)

### 📝 Result
![image](https://github.com/user-attachments/assets/9196688a-6783-4d24-826a-b7db2ec5caf2)

## 🙋‍♂️ Kontributor
Developed by Fahren Alfaqih as part of a web-based Scene Text Recognition (STR) Computer Vision project.

## 📄 Lisensi
MIT License © 2025 Fahren Alfaqih


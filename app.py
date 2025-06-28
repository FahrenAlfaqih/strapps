from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import torch
import torch.nn as nn
import torchvision.transforms as transforms
import io

# ======= Konfigurasi charset dan decoding =======
CHARSET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
idx2char = {i: c for i, c in enumerate(CHARSET)}
num_classes = len(CHARSET)

# ======= Arsitektur Model dari Notebook =======
class SimpleSTR(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.cnn = nn.Sequential(
            nn.Conv2d(1, 64, 3, 1, 1), nn.ReLU(), nn.MaxPool2d(2,2),
            nn.Conv2d(64, 128, 3, 1, 1), nn.ReLU(), nn.MaxPool2d(2,2),
        )
        self.rnn = nn.LSTM(128*8, 256, num_layers=2, bidirectional=True, batch_first=True)
        self.fc = nn.Linear(512, num_classes + 1)  # +1 untuk CTC blank

    def forward(self, x):
        b, c, h, w = x.size()
        x = self.cnn(x)
        x = x.permute(0,3,1,2)
        x = x.reshape(b, 32, 128*8)
        x, _ = self.rnn(x)
        x = self.fc(x)
        return x

# ======= Fungsi Decode CTC Sederhana =======
def decode_ctc(output, blank=num_classes):
    pred_indices = output.argmax(dim=2)  # shape: (B, T)
    pred_str = ""
    prev = -1
    for idx in pred_indices[0]:
        i = idx.item()
        if i != prev and i != blank:
            pred_str += idx2char[i]
        prev = i
    return pred_str

# ======= Setup Flask App =======
app = Flask(__name__)
CORS(app)

# Load model
model = SimpleSTR(num_classes)
model.load_state_dict(torch.load("model_str.pth", map_location=torch.device("cpu")))
model.eval()

# Image transform
transform = transforms.Compose([
    transforms.Resize((32, 128)),  # width 128 sesuai reshape di model
    transforms.ToTensor()
])

@app.route("/predict", methods=["POST"])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    image = Image.open(file.stream).convert("L")
    image = transform(image).unsqueeze(0)  # Add batch dimension

    with torch.no_grad():
        output = model(image)  # shape: (B, T, C)
        prediction = decode_ctc(output)

    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True)

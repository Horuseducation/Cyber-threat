# app.py
from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model and scaler
model = joblib.load("model_rf.joblib")
scaler = joblib.load("scaler.joblib")

# Feature order must match train_model.py cols
FEATURES = ["duration", "src_bytes", "dst_bytes", "wrong_fragment", "urgent", "count", "srv_count", "time_window"]

@app.route("/")
def index():
    return render_template("index.html", features=FEATURES)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    try:
        # collect features in order
        x = [float(data.get(f, 0)) for f in FEATURES]
        x_arr = np.array(x).reshape(1, -1)
        x_scaled = scaler.transform(x_arr)
        prob = model.predict_proba(x_scaled)[0]
        pred = model.predict(x_scaled)[0]
        confidence = float(max(prob))
        label = "Malicious" if int(pred) == 1 else "Benign"
        return jsonify({
            "label": label,
            "confidence": round(confidence, 4),
            "probabilities": {"benign": round(float(prob[0]),4), "malicious": round(float(prob[1]),4)}
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)

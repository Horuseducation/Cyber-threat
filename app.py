from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Safely load model and scaler
model_path = os.path.join(os.path.dirname(__file__), 'model_rf.joblib')
scaler_path = os.path.join(os.path.dirname(__file__), 'scaler.joblib')

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/architecture')
def architecture():
    return render_template('architecture.html')

@app.route('/detect')
def detect():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect form features
        features = [float(x) for x in request.form.values()]
        features = np.array([features])
        scaled = scaler.transform(features)
        prediction = model.predict(scaled)[0]

        result = "Benign (Safe Traffic)" if prediction == 0 else "Malicious (Threat Detected)"
        return render_template('index.html', prediction_text=result)
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)

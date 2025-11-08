from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load your trained model
model = joblib.load('model_rf.joblib')
scaler = joblib.load('scaler.joblib')

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
        # Get features from form
        features = [float(x) for x in request.form.values()]
        features = np.array([features])
        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)[0]

        if prediction == 0:
            result = "Benign (Safe Traffic)"
        else:
            result = "Malicious (Threat Detected)"

        return render_template('index.html', prediction_text=result)
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)

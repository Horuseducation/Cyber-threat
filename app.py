from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load model and scaler
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

@app.route('/detect', methods=['GET', 'POST'])
def detect():
    # Define features
    FEATURES = ['duration', 'src_bytes', 'dst_bytes', 'wrong_fragment', 'urgent', 'count', 'srv_count', 'time_window']

    if request.method == 'POST':
        try:
            data = request.get_json()
            features_list = [float(data[f]) for f in FEATURES]
            features_arr = np.array([features_list])
            scaled = scaler.transform(features_arr)
            prediction = model.predict(scaled)[0]
            proba = model.predict_proba(scaled)[0]

            result = {
                "label": "Benign" if prediction == 0 else "Malicious",
                "confidence": round(max(proba), 3),
                "probabilities": {
                    "benign": round(proba[0], 3),
                    "malicious": round(proba[1], 3)
                }
            }
            return result
        except Exception as e:
            return {"error": str(e)}

    # GET → render template
    return render_template('index.html', features=FEATURES)

if __name__ == '__main__':
    app.run(debug=True)

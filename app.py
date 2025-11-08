from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# ---------- Home Page ----------
@app.route('/')
def home():
    return send_from_directory('web template', 'index.html')

# ---------- Other Static Pages ----------
@app.route('/about')
def about():
    return send_from_directory('web template', 'about.html')

@app.route('/project')
def project():
    return send_from_directory('web template', 'project.html')

@app.route('/contact')
def contact():
    return send_from_directory('web template', 'contact.html')

@app.route('/team')
def team():
    return send_from_directory('web template', 'team.html')

@app.route('/architecture')
def architecture():
    return send_from_directory('web template', 'architecture.html')

@app.route('/overview')
def overview():
    return send_from_directory('web template', 'overview.html')

# ---------- Threat Detection Page ----------
@app.route('/detect')
def detect():
    return render_template('index.html')  # loads templates/index.html

# ---------- Run App ----------
if __name__ == '__main__':
    app.run(debug=True)

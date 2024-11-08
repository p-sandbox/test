# Flask 메인 파일
from flask import Flask, request, jsonify, render_template
from api_routes import analyze_file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file provided"}), 400
    response = analyze_file(file)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

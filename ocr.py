# Save as app.py
from flask import Flask, request, jsonify, send_from_director, send_from_directory
import requests

app = Flask(__name__)

OCR_API_KEY = 'K85888290988957'  # Replace with your actual API key

@app.route("/")
def index():
    return send_from_directory(".", "form.html")

@app.route("/upload", methods=["POST"])
def upload():
    image = request.files.get("image")
    if not image:
        return jsonify({"error": "No image uploaded"}), 400

    response = requests.post(
        "https://api.ocr.space/parse/image",
        files={"file": image},
        data={
            "apikey": OCR_API_KEY,
            "language": "eng"
        },
    )

    result = response.json()
    text = result.get("ParsedResults", [{}])[0].get("ParsedText", "")
    return jsonify({"text": text})

if __name__ == "__main__":
    app.run(debug=True)


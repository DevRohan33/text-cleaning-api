from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def clean_text(text):
    # 1. Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    # 2. Fix spacing after punctuation
    text = re.sub(r"\s*([.?!])\s*", r"\1 ", text)

    # 3. Capitalize first letter of each sentence
    sentences = re.split(r'(?<=[.?!])\s+', text)
    sentences = [s.strip().capitalize() for s in sentences]
    return " ".join(sentences)

@app.route("/clean", methods=["POST"])
def clean_endpoint():
    try:
        data = request.get_json()
        text = data.get("text", "")

        if not text.strip():
            return jsonify({"error": "No text provided."}), 400

        cleaned = clean_text(text)
        return jsonify({
            "cleaned": cleaned
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "<h2> Text Cleaner API is running</h2><p>POST to /clean with JSON {'text': '...'}</p>"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

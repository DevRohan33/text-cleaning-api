import re
import json

def clean_text(text):
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s*([.?!])\s*", r"\1 ", text)
    sentences = re.split(r'(?<=[.?!])\s+', text)
    sentences = [s.strip().capitalize() for s in sentences]
    return " ".join(sentences)

def handler(request):
    try:
        # Decode and parse JSON body from request
        body = request.body.decode("utf-8")
        data = json.loads(body)

        # Check for 'text' key
        text = data.get("text", "").strip()
        if not text:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "No text provided."}),
                "headers": {"Content-Type": "application/json"}
            }

        # Clean the text
        cleaned = clean_text(text)

        return {
            "statusCode": 200,
            "body": json.dumps({"cleaned": cleaned}),
            "headers": {"Content-Type": "application/json"}
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {"Content-Type": "application/json"}
        }

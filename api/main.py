import re

def clean_text(text):
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s*([.?!])\s*", r"\1 ", text)
    sentences = re.split(r'(?<=[.?!])\s+', text)
    sentences = [s.strip().capitalize() for s in sentences]
    return " ".join(sentences)

def handler(request):
    if request.method != "POST":
        return {
            "statusCode": 405,
            "body": "Only POST allowed"
        }

    try:
        data = request.json()
        text = data.get("text", "").strip()

        if not text:
            return {
                "statusCode": 400,
                "body": '{"error": "No text provided."}',
                "headers": {"Content-Type": "application/json"}
            }

        cleaned = clean_text(text)
        return {
            "statusCode": 200,
            "body": f'{{"cleaned": "{cleaned}"}}',
            "headers": {"Content-Type": "application/json"}
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": f'{{"error": "{str(e)}"}}',
            "headers": {"Content-Type": "application/json"}
        }

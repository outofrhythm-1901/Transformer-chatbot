from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


def generate_reply(message: str) -> str:
    """Return a simple demo response without external API dependencies.

    Replace this function with a transformer-model inference call when ready.
    """
    text = message.strip()
    lowered = text.lower()

    if not text:
        return "Please type a message so I can help."
    if any(word in lowered for word in ("hello", "hi", "hey")):
        return "Hi! I'm a demo chatbot. What would you like to explore?"
    if "your name" in lowered or "who are you" in lowered:
        return "I'm a demo chatbot built with Python and Flask."
    if "help" in lowered:
        return "I can respond to simple greetings and questions. Try asking who I am!"
    if any(word in lowered for word in ("thank", "thanks")):
        return "You're welcome!"
    return (
        "That's an interesting question. This starter project currently uses a "
        "simple demo response engine. Connect a pretrained transformer model "
        "to enable richer, context-aware answers."
    )


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "service": "transformer-chatbot-demo"})


@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")

    if not isinstance(message, str):
        return jsonify({"success": False, "error": "The message must be text."}), 400

    if len(message) > 2000:
        return jsonify({"success": False, "error": "Message is too long (maximum 2000 characters)."}), 400

    reply = generate_reply(message)
    return jsonify({"success": True, "reply": reply})


if __name__ == "__main__":
    app.run(debug=True)

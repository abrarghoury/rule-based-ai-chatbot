from flask import Flask, render_template, request, jsonify, session
from chatbot.sanitizer import sanitize
from chatbot.engine    import get_response
from chatbot.context   import session_context
import datetime

app = Flask(__name__)
app.secret_key = "techcorp_secret_2026"

@app.route("/")
def index():
    # Naya page load = fresh context
    session_context.reset()
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data         = request.get_json()
    user_message = data.get("message", "")

    if not user_message.strip():
        return jsonify({"response": "Please type a message."})

    clean  = sanitize(user_message)
    result = get_response(clean)

    return jsonify({
        "response":      result["response"],
        "intent":        result["intent"]["category"],
        "intent_icon":   result["intent"]["icon"],
        "intent_color":  result["intent"]["color"],
        "confidence":    result["confidence"],
        "sentiment":     result["sentiment"]["label"],
        "sentiment_emoji": result["sentiment"]["emoji"],
        "method":        result["method"],
        "timestamp":     datetime.datetime.now().strftime("%I:%M %p")
    })

@app.route("/reset", methods=["POST"])
def reset():
    session_context.reset()
    return jsonify({"status": "Session reset successfully"})

if __name__ == "__main__":
    app.run(debug=True)
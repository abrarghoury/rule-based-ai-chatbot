# Sentiment Analysis — Rule Based + TextBlob
# Detects: positive, negative, neutral, frustrated

from textblob import TextBlob

# Frustrated keywords
FRUSTRATED_KEYWORDS = [
    "useless", "terrible", "worst", "hate", "stupid", "broken",
    "again", "still not", "not working", "fed up", "ridiculous",
    "waste", "pathetic", "disgusting", "awful", "horrible"
]

ANGRY_KEYWORDS = [
    "angry", "furious", "mad", "unacceptable", "demand",
    "immediately", "now", "lawsuit", "refund now", "scam", "fraud"
]

def analyze_sentiment(text):
    text_lower = text.lower()

    # Check frustrated keywords first
    for word in FRUSTRATED_KEYWORDS:
        if word in text_lower:
            return {
                "label": "frustrated",
                "emoji": "😤",
                "score": -0.7,
                "action": "empathize"
            }

    # Check angry keywords
    for word in ANGRY_KEYWORDS:
        if word in text_lower:
            return {
                "label": "angry",
                "emoji": "😠",
                "score": -0.9,
                "action": "escalate"
            }

    # TextBlob for general sentiment
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.3:
        return {
            "label": "positive",
            "emoji": "😊",
            "score": polarity,
            "action": "normal"
        }
    elif polarity < -0.2:
        return {
            "label": "negative",
            "emoji": "😟",
            "score": polarity,
            "action": "empathize"
        }
    else:
        return {
            "label": "neutral",
            "emoji": "😐",
            "score": polarity,
            "action": "normal"
        }
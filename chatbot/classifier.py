# Intent Classifier — categorizes user input into departments
# Returns: category, confidence score, matched keywords

INTENT_CATEGORIES = {
    "Account": {
        "keywords": [
            "password", "login", "account", "locked", "username",
            "email", "signup", "register", "profile", "access"
        ],
        "icon": "🔐",
        "color": "#6366f1"
    },
    "Billing": {
        "keywords": [
            "payment", "invoice", "refund", "subscription", "charge",
            "billing", "plan", "upgrade", "cancel", "receipt", "paid"
        ],
        "icon": "💳",
        "color": "#06b6d4"
    },
    "Technical": {
        "keywords": [
            "error", "bug", "crash", "not working", "slow", "loading",
            "install", "update", "broken", "fix", "issue", "problem"
        ],
        "icon": "🛠",
        "color": "#f59e0b"
    },
    "Security": {
        "keywords": [
            "hacked", "security", "privacy", "breach", "suspicious",
            "unauthorized", "virus", "malware", "data", "stolen"
        ],
        "icon": "🔒",
        "color": "#ef4444"
    },
    "General": {
        "keywords": [
            "help", "hello", "hi", "bye", "thanks", "info",
            "about", "contact", "support", "question"
        ],
        "icon": "💬",
        "color": "#10b981"
    }
}

def classify_intent(clean_input):
    scores = {}
    matched_keywords = {}

    for category, data in INTENT_CATEGORIES.items():
        matched = [kw for kw in data["keywords"] if kw in clean_input]
        scores[category] = len(matched)
        matched_keywords[category] = matched

    best_category = max(scores, key=scores.get)
    best_score    = scores[best_category]
    total_words   = len(clean_input.split())

    # Confidence calculation
    if best_score == 0:
        confidence = 0.2
        best_category = "General"
    else:
        confidence = min(0.95, 0.4 + (best_score / max(total_words, 1)) * 2)

    return {
        "category":         best_category,
        "confidence":       round(confidence, 2),
        "icon":             INTENT_CATEGORIES[best_category]["icon"],
        "color":            INTENT_CATEGORIES[best_category]["color"],
        "matched_keywords": matched_keywords[best_category]
    }
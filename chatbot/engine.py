# Main AI Engine — Fixed Version
# Pipeline: Sanitize → Classify → Sentiment → Match → Context → Respond

from chatbot.responses   import responses
from chatbot.classifier  import classify_intent
from chatbot.sentiment   import analyze_sentiment
from chatbot.fuzzy_match import fuzzy_find
from chatbot.context     import session_context

import random

EMPATHY_RESPONSES = [
    "I'm sorry you're experiencing this. Let me help you right away.\n\n",
    "I understand your frustration. Here's what I found:\n\n",
    "I apologize for the inconvenience. Here's what you can do:\n\n",
]

ESCALATION_RESPONSE = (
    "I can see this issue needs immediate attention.\n"
    "Let me connect you to a live human agent.\n\n"
    "📞 Call Now   : +1-800-TECH-CORP\n"
    "💬 Live Chat  : techcorp.com/chat\n"
    "📧 Email      : support@techcorp.com\n\n"
    "Average wait time: 2-3 minutes."
)

POSITIVE_PREFIXES = [
    "Great! ",
    "Glad to help! ",
    "Sure thing! ",
]

def get_response(clean_input):
    result = {}

    # ── Step 1: Intent Classification ─────────────────
    intent    = classify_intent(clean_input)
    result["intent"] = intent

    # ── Step 2: Sentiment Analysis ────────────────────
    sentiment = analyze_sentiment(clean_input)
    result["sentiment"] = sentiment

    # ── Step 3: Find best response first ──────────────
    reply  = None
    method = None
    conf   = 0.0

    # Exact match
    if clean_input in responses:
        reply  = responses[clean_input]
        method = "exact_match"
        conf   = 0.99

    if not reply:
        # Word level match
        input_words = clean_input.split()
        for key in responses:
            key_words = key.split()
            for word in input_words:
                if word in key_words:
                    reply  = responses[key]
                    method = "keyword_match"
                    conf   = 0.75
                    break
            if reply:
                break

    if not reply:
        # Partial match
        for key in responses:
            if key in clean_input or clean_input in key:
                reply  = responses[key]
                method = "partial_match"
                conf   = 0.60
                break

    if not reply:
        # Fuzzy match
        fuzzy = fuzzy_find(clean_input)
        if fuzzy["matched"]:
            reply  = fuzzy["response"]
            method = "fuzzy_match"
            conf   = round(fuzzy["score"] / 100, 2)

    if not reply:
        reply  = (
            "I'm sorry, I couldn't find a solution for that.\n"
            "Type 'help' to see all topics, or contact us:\n"
            "📧 support@techcorp.com\n"
            "📞 +1-800-TECH-CORP"
        )
        method = "fallback"
        conf   = 0.0

    # ── Step 4: Check Escalation AFTER finding reply ──
    # Only escalate if truly warranted — not on every frustrated message
    if session_context.should_escalate(sentiment["label"], intent["category"]):
        session_context.escalated = True
        result["response"]   = ESCALATION_RESPONSE
        result["confidence"] = 1.0
        result["method"]     = "escalation"
        session_context.update(
            clean_input, ESCALATION_RESPONSE,
            intent["category"], clean_input
        )
        return result

    # ── Step 5: Sentiment-based prefix ───────────────
    if sentiment["action"] == "empathize":
        # Frustrated — empathize but still give the answer
        prefix = random.choice(EMPATHY_RESPONSES)
    elif sentiment["action"] == "normal" and sentiment["score"] > 0.3:
        prefix = random.choice(POSITIVE_PREFIXES)
    else:
        prefix = session_context.get_greeting()

    final_reply = prefix + reply

    # ── Step 6: Repeat warning — only non-General ────
    if session_context.is_repeating(intent["category"]):
        final_reply += (
            "\n\n⚠️ You've asked about "
            + intent["category"]
            + " multiple times. Type 'talk to human' for direct agent support."
        )

    # ── Step 7: Update Context ────────────────────────
    session_context.update(
        clean_input, final_reply,
        intent["category"], clean_input
    )

    result["response"]   = final_reply
    result["confidence"] = conf
    result["method"]     = method

    return result
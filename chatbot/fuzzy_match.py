# Fuzzy Matching — handles spelling mistakes
# Uses Levenshtein distance for similarity scoring

from fuzzywuzzy import fuzz
from chatbot.responses import responses

def fuzzy_find(clean_input, threshold=65):
    best_match = None
    best_score = 0

    for key in responses:
        # Token sort ratio handles word order differences
        score = fuzz.token_sort_ratio(clean_input, key)

        if score > best_score:
            best_score = score
            best_match = key

    if best_score >= threshold:
        return {
            "key":      best_match,
            "response": responses[best_match],
            "score":    best_score,
            "matched":  True
        }

    return {
        "key":      None,
        "response": None,
        "score":    best_score,
        "matched":  False
    }
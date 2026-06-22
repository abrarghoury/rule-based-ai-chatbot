# Phase 1: Input Sanitization
# Removes extra spaces and converts to lowercase

def sanitize(raw_input):
    clean_input = raw_input.lower().strip()
    return clean_input
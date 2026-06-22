# Entry Point — The Infinite Loop (Heartbeat)
# Project 1: Rule-Based AI Chatbot
# DecodeLabs Industrial Training — Batch 2026

from chatbot.sanitizer import sanitize
from chatbot.engine import get_response

def main():
    print("=" * 50)
    print("   Welcome to DecoBot — Rule-Based AI Chatbot")
    print("   Powered by DecodeLabs | Batch 2026")
    print("=" * 50)
    print("   Type 'help' for commands | Type 'quit' to exit")
    print("=" * 50)
    print()

    while True:
        raw_input = input("You: ")

        # Exit Strategy — Kill Command
        if raw_input.lower().strip() in ["quit", "exit", "q"]:
            print("DecoBot: Goodbye! Session ended. Keep building!")
            break

        # Sanitize Input
        clean = sanitize(raw_input)

        # Get Response from Engine
        response = get_response(clean)

        print(f"DecoBot: {response}")
        print()

if __name__ == "__main__":
    main()
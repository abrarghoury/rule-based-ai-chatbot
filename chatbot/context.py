# Context Memory — Fixed Version
# Escalation sirf tab ho jab same issue 3+ baar aaye
# Ya user explicitly angry ho

class ConversationContext:
    def __init__(self):
        self.history            = []
        self.user_name          = None
        self.last_category      = None
        self.category_count     = {}   # per category count
        self.last_intent_key    = None # exact last intent track
        self.same_intent_streak = 0    # same intent kitni baar
        self.escalated          = False
        self.message_count      = 0
        self.angry_count        = 0    # kitni baar angry sentiment

    def update(self, user_msg, bot_reply, category, intent_key=None):
        self.history.append({
            "user":     user_msg,
            "bot":      bot_reply,
            "category": category
        })
        self.message_count += 1

        # Same intent streak track karo
        if intent_key and intent_key == self.last_intent_key:
            self.same_intent_streak += 1
        else:
            self.same_intent_streak = 0
            self.last_intent_key    = intent_key

        self.last_category = category

        # Per category count — General ko count mat karo
        if category != "General":
            self.category_count[category] = \
                self.category_count.get(category, 0) + 1

    def should_escalate(self, sentiment_label, category):
        # Escalate sirf agar:
        # 1. User explicitly angry ho (not just frustrated)
        if sentiment_label == "angry":
            self.angry_count += 1
            # Ek angry message escalate nahi karta —
            # 2 angry messages pe escalate karo
            if self.angry_count >= 2:
                return True

        # 2. Same exact intent 3+ baar aaye (alag category nahi)
        if (self.same_intent_streak >= 3 and category != "General"):
            return True

        # 3. Pehle se escalate ho chuka hai toh dobara mat karo
        if self.escalated:
            return False

        return False

    def is_repeating(self, category):
        # Sirf non-General category mein 3+ baar same issue
        if category == "General":
            return False
        return self.category_count.get(category, 0) >= 3

    def get_greeting(self):
        if self.user_name:
            return f"Got it, {self.user_name}! "
        return ""

    def set_user_name(self, name):
        self.user_name = name.strip().capitalize()

    def reset(self):
        self.__init__()


# Global session context
session_context = ConversationContext()
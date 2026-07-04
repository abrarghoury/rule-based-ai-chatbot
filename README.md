# 🤖 TechCorp AI Help Desk Chatbot

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?style=flat-square&logo=flask)
![AI](https://img.shields.io/badge/AI-Rule--Based-6366f1?style=flat-square)
![NLP](https://img.shields.io/badge/NLP-TextBlob%20%7C%20FuzzyWuzzy-06b6d4?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-10b981?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

> A production-ready, rule-based AI Help Desk Chatbot built with Python and Flask — featuring Sentiment Analysis, Intent Classification, Fuzzy Matching, and Context Memory. 
---

## 📸 Preview

```
┌─────────────────────────────────────────────────────────┐
│  TechCorp AI Help Desk — DecoBot v2.0                   │
│  Sentiment · Intent · Fuzzy Match · Context Memory      │
├──────────────┬──────────────────────────────────────────┤
│  SIDEBAR     │  CHAT WINDOW                             │
│              │                                          │
│  Navigation  │  You: forgot password                   │
│  AI Metrics  │  DecoBot: To reset your password...     │
│  Session     │  🔐 Account  ⚡ 99%  😐 neutral         │
│  Info        │  🔍 exact match                         │
└──────────────┴──────────────────────────────────────────┘
```

---

## 🧠 AI Concepts Used

| Concept | Implementation | Module |
|---|---|---|
| **Intent Classification** | Keyword-based category detection | `classifier.py` |
| **Sentiment Analysis** | TextBlob + custom keyword rules | `sentiment.py` |
| **Fuzzy Matching** | Levenshtein distance via FuzzyWuzzy | `fuzzy_match.py` |
| **Context Memory** | Session-based conversation tracking | `context.py` |
| **Escalation Logic** | Anger detection + repeat issue tracking | `engine.py` |
| **O(1) Hash Map Lookup** | Python dictionary as knowledge base | `responses.py` |
| **IPO Architecture** | Input → Process → Output pipeline | All modules |

---

## ⚙️ Features

- **30+ Predefined Intents** — Account, Billing, Technical, Security, General
- **4-Layer Matching Engine** — Exact → Keyword → Partial → Fuzzy
- **Real-time Sentiment Detection** — Positive, Neutral, Frustrated, Angry
- **Smart Escalation** — Auto-escalates after 2 angry messages or 3 repeated issues
- **Context Memory** — Tracks conversation history within session
- **Live AI Metrics Dashboard** — Confidence score, fallback rate, match method
- **Session Management** — Start, end, and reset sessions cleanly
- **Professional Dark UI** — TechCorp-styled Help Desk dashboard

---

## 📁 Project Structure

```
rule_based_chatbot/
│
├── chatbot/
│   ├── __init__.py          # Package initializer
│   ├── responses.py         # Knowledge base — 30+ intents dictionary
│   ├── sanitizer.py         # Input sanitization (lowercase + strip)
│   ├── classifier.py        # Intent classification by category
│   ├── sentiment.py         # Sentiment analysis (TextBlob + keywords)
│   ├── fuzzy_match.py       # Fuzzy string matching
│   ├── context.py           # Session context and memory
│   └── engine.py            # Core AI pipeline engine
│
├── templates/
│   └── index.html           # Frontend dashboard (HTML + CSS + JS)
│
├── app.py                   # Flask server
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
└── README.md                # This file
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or above
- pip package manager

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/rule_based_chatbot.git
cd rule_based_chatbot
```

**2. Create virtual environment**
```bash
python -m venv venv
```

**3. Activate virtual environment**
```bash
# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

**4. Install dependencies**
```bash
pip install -r requirements.txt
```

**5. Run the application**
```bash
python app.py
```

**6. Open in browser**
```
http://127.0.0.1:5000
```

---

## 💬 Supported Intents

### 🔐 Account
`forgot password` · `reset password` · `account locked` · `cannot login` · `login issue` · `change password` · `account suspended`

### 💳 Billing
`billing` · `invoice` · `payment failed` · `refund` · `subscription` · `cancel subscription` · `upgrade plan`

### 🛠 Technical
`app not working` · `app crash` · `slow performance` · `not loading` · `error 404` · `error 500` · `server down` · `bug` · `how to install` · `update`

### 🔒 Security
`hacked` · `security` · `privacy` · `two factor` · `data backup` · `data lost`

### 📞 Contact
`contact support` · `talk to human` · `complaint` · `feedback` · `escalate`

---

## 🔬 How The AI Pipeline Works

```
User Input
    │
    ▼
┌─────────────┐
│  Sanitizer  │  lowercase + strip whitespace
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Classifier │  Detect intent category (Account/Billing/Technical/Security/General)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Sentiment  │  Analyze mood (positive/neutral/frustrated/angry)
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────┐
│  4-Layer Matching Engine        │
│  1. Exact Match      → 99%      │
│  2. Keyword Match    → 75%      │
│  3. Partial Match    → 60%      │
│  4. Fuzzy Match      → 45-80%   │
│  5. Fallback         → 0%       │
└──────┬──────────────────────────┘
       │
       ▼
┌─────────────┐
│   Context   │  Check session history, repeat detection, escalation
└──────┬──────┘
       │
       ▼
   Final Reply
```

---

## 🛡️ Escalation Logic

The bot automatically escalates to human support when:

- User sends **2 angry messages** in a session
- User asks about the **same category 3+ times**
- User types `talk to human`

---

## 📊 Dashboard Metrics

| Metric | Description |
|---|---|
| **Confidence Score** | How certain the bot is about its response (0–99%) |
| **Fallback Rate** | % of messages the bot could not understand |
| **Match Method** | Which matching layer resolved the query |
| **Intent Badge** | Category of the detected user intent |
| **Sentiment** | Detected emotional tone of the message |
| **Session Timer** | Live duration of the current session |

---

## 🧪 Test Cases

| Input | Expected Intent | Expected Method |
|---|---|---|
| `forgot password` | Account | Exact Match |
| `forgt passwrd` | Account | Fuzzy Match |
| `payment failed` | Billing | Exact Match |
| `this is useless` | General | Fallback + Empathy |
| `thank you` | General | Exact Match |
| `xyz abc 123` | General | Fallback |
| `scam` + `refund now` | Billing | Escalation |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.10, Flask 3.0 |
| NLP | TextBlob, FuzzyWuzzy, python-Levenshtein |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Fonts | Google Fonts — Inter |
| Icons | Font Awesome 6.4 |
| Environment | python-dotenv |

---

## 📦 Dependencies

```
flask
textblob
fuzzywuzzy
python-Levenshtein
python-dotenv
```

---

## 🔮 Future Improvements

- [ ] Machine Learning intent classifier (scikit-learn)
- [ ] Multi-language support (Urdu + English)
- [ ] Admin panel to add/edit responses live
- [ ] Chat export to PDF
- [ ] Database integration for persistent sessions
- [ ] REST API for third-party integration

---

## 👨‍💻 Author

Abrar Shakeel 
---

## 📄 License

This project is licensed under the MIT License.

---

> *"Before you can manage the chaos of a probability engine, you must master the precision of a logic engine."*


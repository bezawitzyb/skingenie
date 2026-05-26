# 🧴 SkinGenie — AI-Powered Skincare Routine Generator

> A data science & AI portfolio project that generates personalized weekly skincare routines based on your products and skin concerns.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![Claude API](https://img.shields.io/badge/AI-Claude%20API-purple)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Features

### V1 — Text-Based Routine Generator (current)
- Input your skincare products and skin concerns
- Get a personalized 7-day AM/PM routine powered by Claude AI
- Ingredient conflict warnings (e.g. Retinol + AHAs)

### V2 — Data Science Layer (coming soon)
- Ingredient database with real product data
- RAG-powered recommendations grounded in facts

### V3 — Computer Vision (coming soon)
- Upload a photo of your face
- AI detects skin concerns automatically

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/skingenie.git
cd skingenie
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key
```bash
cp .env.example .env
# Open .env and add your Claude API key
```

Get your free API key at: https://console.anthropic.com

### 5. Run the app
```bash
streamlit run app.py
```

---

## 🗂️ Project Structure

```
skingenie/
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
├── .gitignore              # Files to exclude from git
├── README.md               # You are here
│
├── src/
│   ├── __init__.py
│   ├── llm.py              # Claude API calls & prompt logic
│   ├── routine.py          # Routine formatting & display
│   └── validator.py        # Input validation helpers
│
└── data/
    └── ingredients.csv     # Ingredient conflict database (V2)
```

---

## 🧠 What This Project Teaches

| Skill | Where Used |
|---|---|
| Prompt Engineering | `src/llm.py` — crafting structured LLM outputs |
| Python & APIs | `src/llm.py` — calling Claude REST API |
| Data Wrangling | `data/` — pandas ingredient processing (V2) |
| RAG | Grounding LLM in real ingredient data (V2) |
| Computer Vision | Face analysis with vision models (V3) |
| App Deployment | Streamlit Community Cloud |

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **UI:** Streamlit
- **AI:** Anthropic Claude API
- **Data:** pandas, INCIDecoder dataset
- **Deployment:** Streamlit Community Cloud (free)

---

## 📄 License

MIT — feel free to fork, extend, and use this in your own portfolio.

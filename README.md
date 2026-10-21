# Transformer-Based Chatbot

A small, beginner-friendly chatbot web app built with **Python, Flask, and a lightweight React-free HTML/CSS/JavaScript interface**. It demonstrates a clean API flow, input validation, fallback responses, and a simple chat UI.

> **Important:** This is a portfolio starter project, not a trained transformer model. The included response engine uses a transparent rule-based fallback so it runs locally without API keys or paid services. You can later connect a real transformer model.

## Features

- Chat interface with message history
- Python Flask REST API (`POST /api/chat`)
- Input validation and friendly fallback responses
- Health-check endpoint (`GET /api/health`)
- Clear separation between frontend and backend
- No secrets or external services required

## Tech stack

- Python 3.10+
- Flask
- HTML, CSS, JavaScript
- REST API / JSON

## Project structure

```text
transformer-chatbot/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── app.js
```

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment (optional but recommended).

   **Windows**
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   python app.py
   ```
6. Open http://127.0.0.1:5000 in your browser.

## API example

Request:
```bash
curl -X POST http://127.0.0.1:5000/api/chat \
  -H "Content-Type: application/json" \
  -d "{\"message\":\"Hello\"}"
```

Example response:
```json
{
  "reply": "Hi! I'm a demo chatbot. What would you like to explore?",
  "success": true
}
```

## Future improvements

- Replace the demo response engine with a pretrained transformer model
- Add automated tests and conversation persistence
- Add rate limiting and structured logging
- Deploy the app to a hosting platform

## Author

GitHub: https://github.com/outofrhythm-1901

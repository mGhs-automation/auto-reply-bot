# 📧 Email Auto-Reply Bot

Automate your inbox! This Python tool reads unread emails and sends smart replies automatically.  
Built with **Python**, **Gmail API**, and optional **OpenAI integration** for AI-powered responses.

---

## 🔧 Features
- Check unread emails
- Classify messages (spam / inquiry / urgent)
- Auto-reply with **custom templates** or **AI-generated replies**
- Gmail API integration
- Optional: Google Sheets tracking for processed emails

---

## 🚀 Installation

1. **Clone the repo**
```bash
git clone https://github.com/mGhs-automation/auto-reply-bot.git
cd auto-reply-bot

pip install -r requirements.txt

python main.py

📂 Example Output

Found 4 unread emails.
Processing email from John with subject 'Need automation help'...
Reply sent!

⚡ Optional AI Integration

Add your OpenAI API key to use auto-generated replies

Modify main.py to enable AI response logic
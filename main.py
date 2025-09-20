# Email Sorting & Auto-Reply Bot Template
import imaplib
import email
import smtplib
from email.mime.text import MIMEText
from openai import OpenAI

# ---------- CONFIG ----------
EMAIL_ADDRESS = "dha77aren19@gmail.com"
EMAIL_APP_PASSWORD = "vyus vakq spjs rpqa"
OPENAI_API_KEY = ""
IMAP_SERVER = "imap.gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# Initialize OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

# ---------- FUNCTIONS ----------
def classify_email(body):
    body = body.lower()
    if "invoice" in body or "price" in body:
        return "lead"
    elif "help" in body or "support" in body:
        return "support"
    elif "win" in body or "prize" in body:
        return "spam"
    else:
        return "other"


def generate_reply(category):
    """Generate a simple reply based on category"""
    if category.lower() == "lead":
        return "Hi! Thank you for your interest. I will contact you shortly."
    elif category.lower() == "support":
        return "Hi! We received your support request and will respond soon."
    elif category.lower() == "spam":
        return None  # No reply for spam
    else:
        return "Thank you for your email."

def send_email(to_email, subject, body):
    """Send an email via SMTP"""
    msg = MIMEText(body)
    msg['Subject'] = f"Re: {subject}"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email

    server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    server.login(EMAIL_ADDRESS, EMAIL_APP_PASSWORD)
    server.send_message(msg)
    server.quit()
    print(f"Replied to {to_email}")

# ---------- MAIN ----------
def check_and_reply():
    # Connect to Gmail inbox
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ADDRESS, EMAIL_APP_PASSWORD)
    mail.select("inbox")

    status, messages = mail.search(None, '(UNSEEN)')
    mail_ids = messages[0].split()

    print(f"Found {len(mail_ids)} unread emails.")

    for mail_id in mail_ids:
        status, msg_data = mail.fetch(mail_id, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])

        sender = msg['from']
        subject = msg['subject']
        body = ""
        if msg.is_multipart():
            for part in msg.get_payload():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
        else:
            body = msg.get_payload(decode=True).decode()

        print(f"Processing email from {sender} with subject '{subject}'")

        # Classify email
        category = classify_email(body)
        print(f"Category: {category}")

        # Generate reply
        reply_text = generate_reply(category)
        if reply_text:
            send_email(sender, subject, reply_text)

    mail.logout()

# Run the bot
if __name__ == "__main__":
    check_and_reply()

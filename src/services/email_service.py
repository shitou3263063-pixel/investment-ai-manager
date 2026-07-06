from __future__ import annotations

import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv


def send_email_if_configured(subject: str, body: str) -> bool:
    load_dotenv()

    host = os.getenv("SMTP_HOST")
    port = int(os.getenv("SMTP_PORT", "587"))
    user = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASSWORD")
    to = os.getenv("EMAIL_TO")

    if not all([host, user, password, to]):
        print("Email not configured, skipped.")
        return False

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = user
    msg["To"] = to

    try:
        if port == 465:
            with smtplib.SMTP_SSL(host, port, timeout=30) as server:
                server.login(user, password)
                server.sendmail(user, [to], msg.as_string())
        else:
            with smtplib.SMTP(host, port, timeout=30) as server:
                server.starttls()
                server.login(user, password)
                server.sendmail(user, [to], msg.as_string())

        print("Email sent.")
        return True

    except Exception as e:
        print("Email send failed:", e)
        return False

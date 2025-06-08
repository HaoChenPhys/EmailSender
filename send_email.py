#!/usr/bin/env python3
"""
send_scores.py ­– email every student their individual score.

* Requires Python ≥3.8.
* Uses the standard-library `email` and `smtplib` modules.
* Reads SMTP credentials from environment variables so you never
  hard-code passwords.

Usage:
    $ export SMTP_HOST="smtp.gmail.com"
    $ export SMTP_PORT="465"             # 587 if you prefer STARTTLS
    $ export SMTP_USERNAME="you@example.com"
    $ export SMTP_PASSWORD="your-app-specific-password"
    $ python send_email.py
"""

import os
import smtplib
import json
from email.message import EmailMessage
from typing import Dict, Tuple

# ---------------------------------------------------------------------------
# 1.  Your student data  – adapt as needed
# ---------------------------------------------------------------------------
# with open('data.json', 'r', encoding='utf-8') as f:
#     students = json.load(f)
students: Dict[str, Tuple[str, int]] = {
    "Alice": ("alice123@example.com", 92),
    "Bob":   ("bob456@example.com",   78),
    # …
}


# ---------------------------------------------------------------------------
# 2.  Configuration – NEVER hard-code secrets
# ---------------------------------------------------------------------------
SMTP_HOST: str = os.getenv("SMTP_HOST", "")
SMTP_PORT: int = int(os.getenv("SMTP_PORT", "465"))
SMTP_USERNAME: str = os.getenv("SMTP_USERNAME", "")
SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "")
FROM_ADDR: str = SMTP_USERNAME            # sender shown in the e-mail header

if not all((SMTP_HOST, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD)):
    raise SystemExit(
        "❌  Missing one or more SMTP_* environment variables – aborting."
    )

# ---------------------------------------------------------------------------
# 3.  Helper: build and send one message
# ---------------------------------------------------------------------------
def send_score(name: str, email: str, score: int, server: smtplib.SMTP) -> None:
    """Compose and send a plain-text e-mail with the student’s score."""
    msg = EmailMessage()

    # --- headers ---
    msg["Subject"] = "Linear Algebra II exam score"
    msg["From"] = FROM_ADDR
    msg["To"] = email

    # --- body ---
    msg.set_content(
        f"""\
Hi {name},

Your score for the Linear Algebra II exam is {score} on a 1-6 scale.
The exam is officially graded pass/fail; the numeric score reported here is purely for your own reference.
A score of 4 or higher counts as a pass.

Best regards,
the TA Team
"""
    )

    # --- send ---
    server.send_message(msg)
    print(f"✅  Sent to {name} ({email})")


# ---------------------------------------------------------------------------
# 4.  Main routine: open one SMTP connection, reuse it for all students
# ---------------------------------------------------------------------------
def main() -> None:
    # Change SSL->STARTTLS if you use port 587
    with smtplib.SMTP_SSL(host=SMTP_HOST, port=SMTP_PORT) as server:
        server.login(SMTP_USERNAME, SMTP_PASSWORD)

        for name, (email, score) in students.items():
            send_score(name, email, score, server)


if __name__ == "__main__":
    main()

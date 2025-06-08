# Tool for emails sending

## Usage

````
    $ export SMTP_HOST="smtp.gmail.com"
    $ export SMTP_PORT="465"             # 587 if you prefer STARTTLS
    $ export SMTP_USERNAME="you@example.com"
    $ export SMTP_PASSWORD="your-app-specific-password"
    $ python send_email.py
````

## Gmail login

* Turn on 2-Step Verification for the Google account if it isn’t already.
* Visit Google Account ▸ Security ▸ “App passwords”.
* Pick Mail as the app and either leave the device as “Other” or give it a name like “Python SMTP”.
* Google shows a 16-character code once. Copy it and use it for SMTP_PASSWORD.
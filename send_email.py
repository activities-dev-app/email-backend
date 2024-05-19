import os
from dotenv import load_dotenv

load_dotenv()


def send_email(to_addr: str, subject: str, body: dict):
    import smtplib

    #https://stackoverflow.com/questions/882712/send-html-emails-with-python

    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    app_password = os.environ.get("APP_PASSWORD")
    service_email = os.environ.get("SERVICE_EMAIL")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = service_email
    msg["To"] = to_addr

    text = body["text"]
    html = body["html"]

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    msg.attach(part1)
    msg.attach(part2)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=service_email, password=app_password)
        connection.sendmail(
            from_addr=service_email,
            to_addrs=to_addr,
            msg=msg.as_string(),
        )

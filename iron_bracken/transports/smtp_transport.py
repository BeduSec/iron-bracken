import smtplib
from email.mime.text import MIMEText

class SMTPTransport:
    def __init__(self, server, port=25):
        self.server = server
        self.port = port

    def send(self, sender, recipient, data):
        msg = MIMEText(data)
        msg['Subject'] = 'Status Update'
        try:
            with smtplib.SMTP(self.server, self.port, timeout=5) as smtp:
                smtp.sendmail(sender, recipient, msg.as_string())
            return True
        except Exception:
            return False

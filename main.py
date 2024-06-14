from email.mime.text import MIMEText
import smtplib
import os
from dotenv import load_dotenv


def send_mail(msg_value):
    msg = MIMEText(msg_value)
    
    msg['Subject'] = "Gemini Report"
    msg['From'] = sender_email
    msg['To'] = to_email

    with smtplib.SMTP(smtp_server, port) as server:
      server.starttls()  
      server.login(sender_email, password)
      server.sendmail(sender_email, to_email, msg.as_string())
def read_file(path):
    if not os.path.exists(path):
        return "not found"
    with open(path, "r") as f:
        return f.read()


load_dotenv()


smtp_server = os.getenv("smtp_server")
port = os.getenv("port")
sender_email = os.getenv("sender_email")
password = os.getenv("password") 

to_email = os.getenv("to_mail")

mail_msg_path = os.getenv("mail_msg_path")

msg_value = read_file(mail_msg_path)
send_mail(msg_value)
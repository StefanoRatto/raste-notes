import smtplib

from email import encoders
from email.mime.text import MIMEText
#from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()

server.login("0x7261737465@gmail.com", "Minim@l2")

msg = MIMEMultipart()
msg["From"] = "raste"
msg["To"] = "stefano.ratto@gmail.com"
msg["Subject"] = "Just a test, hi from Python"

with open("message.txt", "r") as f:
    message = f.read()

msg.attach(MIMEText(message, "plain"))

text = msg.as_string()

server.sendmail("0x7261737465@gmail.com", "stefano.ratto@gmail.com", text)















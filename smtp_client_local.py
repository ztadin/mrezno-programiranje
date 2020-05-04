import smtplib
import email.utils
from email.mime.text import MIMEText

to = input("To: ")
subject = input("Subject: ")
body = input("Body: ")

msg = MIMEText(body)
msg['To'] = email.utils.formataddr(('Recipient', to))
msg['From'] = email.utils.formataddr(('Author', 'test@test.com'))
msg['Subject'] = subject

server = smtplib.SMTP('127.0.0.1', 1025)
server.sendmail('test@test.com', [to], msg.as_string())
server.close()
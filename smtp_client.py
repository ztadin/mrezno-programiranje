import smtplib
import email.utils
from email.mime.text import MIMEText

host = "smtp.mailtrap.io"
port = 2525
user = ""
password = ""

to = input("To: ")
subject = input("Subject: ")
body = input("Body: ")

msg = MIMEText(body)
msg['To'] = email.utils.formataddr(('Recipient', to))
msg['From'] = email.utils.formataddr(('Author', 'test@test.com'))
msg['Subject'] = subject

server = smtplib.SMTP(host, 2525)
server.login(user, password)
server.sendmail('test@test.com', [to], msg.as_string())
server.close()
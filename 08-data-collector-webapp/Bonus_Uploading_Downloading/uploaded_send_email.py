from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email = "data.web.app.height"
    from_password = "RD&ts#qpQo#&8FtJ"
    to_email = email

    subject = "Height data"
    message = "Hey there, your height is <strong>%s</strong>. Average height of all is <strong>%s</strong>. This is based on <strong>%s</strong> people" % (height, average_height, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)

    # In gmail need to allow less secure methods to login to your account


This was added later!
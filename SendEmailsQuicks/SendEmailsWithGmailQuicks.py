"""
Send Emails
"""

import smtplib
from email.message import EmailMessage
import imghdr

PORT = 587

Your_Email = 'yours@email.com'
Your_Password = 'password'

receiver = input("Send To: ")
__receiver__ = f'{receiver}'
subject = input("Email Subject: ")
__subject__ = f'{subject}'
content = input("Email Content: ")
__content__ = f'{content}'

with smtplib.SMTP('smtp.gmail.com', PORT) as send__mail:
    send__mail.starttls()
    send__mail.login(Your_Email, Your_Password)

    message = EmailMessage()
    message['From'] = Your_Email
    message['To'] = __receiver__
    message['Subject'] = __subject__
    message.set_content(__content__)

    with open('pictures/file', 'rb') as image_attachment:
        img = image_attachment.read()
        img_type = imghdr.what(image_attachment.name)
    message.add_attachment(img, maintype='image', subtype=img_type)

    send__mail.send_message(message)

    print("An Email Has Been Sent!")

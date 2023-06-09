import datetime
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_mail():
    print("Sending report email")
    # SMTP server configuration
    smtp_server = 'aspmx.l.plydot.com'
    smtp_port = 587

    # Email login credentials
    sender_email = 'info@sk-engine.cloud'
    sender_password = 'nomisr123'

    # Recipient email address
    recipient_email = os.environ.get('LOGS_RECIPIENT_EMAIL', 'srmugisa@gmail.com')

    # Email content
    subject = 'Records Submitted'
    body = 'Find attached logs for successful and failed records'

    # Create a multipart message object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    message['Cc'] = 'whippetwilson@gmail.com'

    print(message)
    # Attach the body to the message
    message.attach(MIMEText(body, 'plain'))

    # Attach first file
    attachment1 = MIMEBase('application', 'octet-stream')
    with open('error_logs.txt', 'rb') as file1:
        attachment1.set_payload(file1.read())
    encoders.encode_base64(attachment1)
    attachment1.add_header('Content-Disposition', 'attachment', filename='error_logs.txt')
    message.attach(attachment1)

    # Attach second file
    attachment2 = MIMEBase('application', 'octet-stream')
    with open('success_logs.txt', 'rb') as file2:
        attachment2.set_payload(file2.read())
    encoders.encode_base64(attachment2)
    attachment2.add_header('Content-Disposition', 'attachment', filename='success_logs.txt')
    message.attach(attachment2)

    try:
        # Establish a secure connection with the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            # Log in to the sender's email account
            server.login(sender_email, sender_password)
            # Send the email
            server.send_message(message)
            print("Email sent successfully!")
            # Delete the attached files
            os.rename('success_logs.txt', f"success_logs_{datetime.datetime.now().strftime('%Y_%m_%dT%H.%M.%S')}.txt")
            os.rename('error_logs.txt', f"error_logs_{datetime.datetime.now().strftime('%Y_%m_%dT%H.%M.%S')}.txt")
    except Exception as e:
        print("Error occurred while sending the email:", str(e))

import smtplib
import time
from email.message import EmailMessage

sender = "jameshansson21@gmail.com"
password = "uwktojrmoseksnra"
recipients_str = input("Enter recipient email address: ")
recipients = recipients_str.split(",")
subject = input("Subject of the mail: ")
name = input("Input your name: ")
body = input("Enter email body: ")
def send_email():
    msg = EmailMessage()
    msg.set_content(body)
    msg['From'] = f"{sender}, {name}"
    msg['To'] = recipients_str
    msg['Subject'] = subject

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)
        print("Message sent successfully")

counter = 0  # Counter to keep track of the number of iterations
while counter < 4:  # Loop until the counter reaches 4
    counter += 1  # Increment the counter after each email sent
    send_email()
    time.sleep(60)  # Sleep for 1 minutes (60 seconds)
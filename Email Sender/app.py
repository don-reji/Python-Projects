from email.message import EmailMessage
import smtplib
import ssl

email_sender=input("Enter your email: ")

email_password=input("Enter your app password: ")   
#use app password, refer to readme.md for more info
# note that this doesn't store your password anywhere, it just uses it to login to your email account

email_recevier=input("Enter the email of the recevier: ")

subject='This is a test email'

body='Hello there, this is a test email. Have a good day!'

# creating an instance of EmailMessage
em=EmailMessage()

# Setting Message Headers
em['From']=email_sender
em['To']=email_recevier
em['Subject']=subject
em.set_content(body)
#em.set_content is the body of the email

# creating a secure connection for sending email
context=ssl.create_default_context()

# creating a smtp server
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_recevier, em.as_string())
    print("Email sent successfully")
# The code is responsible for sending an email using the SMTP_SSL class from the smtplib library 
# in Python. It establishes a secure connection to Gmail's SMTP server (smtp.gmail.com) on port 465 using 
# SSL/TLS encryption, logs in with the sender's email credentials, sends an email, and then prints a success
#  message.








# Email Sender
## Introduction
This is a email sender using python for sending email messages.

*Note- You need to generate app password for your email account, check below. This doesn't store your password anywhere, it just uses it to login to your email account
## Table Of Content
- [Introduction](#introduction)
- [Explanation](#explanation)
- [Generate App Password](#generate-email-app-password)
- [Usage](#usage)

## Explanation
app.py uses 3 standard library modules.
```python
from email.message import EmailMessage
import smtplib
import ssl
```

1. email.message - Provides classes and functions for working with email messages, including the EmailMessage class.
2. smtplib - Provides classes and functions for sending email using the Simple Mail Transfer Protocol (SMTP).
3. ssl - Provides functionality for working with Secure Sockets Layer (SSL) and Transport Layer Security (TLS) encryption protocols. The ssl module allows you to create SSL/TLS contexts, establish secure connections, and configure various SSL/TLS-related settings.

## Generate Email App Password
Instead of using your email account password to login, we generate 'app password' for your email account to use. 

Here's how to generate it:

1. Login to your gmail account from which you want to send the email.
2. Then go to [this link.]()
3. Enable 2-step verification.
4. In the searchbar above search for 'App Passwords' and select it.
5. In the 'select app' , select 'other' and type 'python'. It then generates an app password, copy it for using in this project.

*Note- This is not your email password.

## Usage
1. Run app.py, when prompted to enter email_sender, email_password and email_receiver. If the email has been sent successfully it shows.
   



import smtplib
import imaplib
import sys

from email.parser import Parser as EmailParser

def send_mail(from_credentials, to_email, body, subject=""):
    # TODO: Need some error handling...
    message = "\r\n".join([
        "From: user_me@gmail.com",
        "To: ", to_email,
        "Subject: ", subject,
        "",
        body])

    # Sending the mail  
    
    server = smtplib.SMTP(from_credentials['server']['smtp'])
    server.ehlo()
    server.starttls()
    server.login(from_credentials['email'], from_credentials['password'])
    server.sendmail(from_credentials['email'], to_email, message)
    server.quit()

def imap_connect(credentials):
    mail = imaplib.IMAP4_SSL(credentials['server']['imap'])
    try:
        (return_code, capabilities) = mail.login(credentials['email'], credentials['password'])
    except:
        # TODO: HAH. This is stupid.
        print(sys.exc_info()[1])
        sys.exit(1)
    return mail 

def check_mail(credentials, label='INBOX'):
    mail = imap_connect(credentials)
    try:
        response, data = mail.select(label)
        if response == 'OK':
            response, message_ids = mail.uid('search', None, '(UNSEEN)')
            if len(message_ids[0]) == 0:
                return None
            response, message_data = mail.uid('fetch', ','.join(message_ids[0].decode().split()), '(RFC822)')
            return [msg[1].decode() for msg in message_data if isinstance(msg, tuple)]
    finally:
        try:
            mail.close()
        except:
            pass
        print('logging out')
        mail.logout()


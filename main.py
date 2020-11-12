import imaplib
import email
import os
import webbrowser
from email.header   import decode_header
from dateutil.parser import*
import time 
from datetime import datetime
import smtplib, ssl
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class login:
    def __init__(self):
    
        self.username='example@gmail.com'
        self.
        ord='password'
        self.port = 465  # For SSL
        self.smtp_server = "smtp.gmail.com"
   
     
        self.imap = imaplib.IMAP4_SSL('imap.gmail.com')
        self.imap.login(self.username,self.password)
        self.imap.select()
    @staticmethod
    def time_data(y):
        y=str(y)
        #y=str(y)
        x=datetime.fromisoformat(y)
        return(x.timestamp())


       
    def last_reply(self):
        typ,data=self.imap.search(None,'(FROM "example@gmail.com")')
        self.imap.select()
        self.l=[]
        for num in data[0].split():
            typ,data=self.imap.fetch(num,('RFC822'))
            raw_email_string=data[0][1].decode('utf-8')
            msg=email.message_from_string(raw_email_string)
    
            dats=parse(msg['Date'])
            
            self.l.append(login.time_data(dats))
        return self.l
   
    def last_sent(self):
        
    
        res,data2=self.imap.search(None,'(TO "example@gmail.com")')
        self.imap.select()
        self.l2=[]
        for num in data2[0].split():
            
            res,data2=self.imap.fetch(num,('RFC822'))
            raw_email_string=data2[0][1].decode('utf-8')
            msg2=email.message_from_string(raw_email_string)
            #dat=parse(msg2['Date'])
            
            #self.l2.append(login.time_data(dat))
            print(msg2)
    def sendmail(self):
        

        

        receiver_email = "example@gmail.com"  # Enter receiver address

        message = """\
        Subject: Hi there

        This message is to check up on you."""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
            server.login(self.username, self.password)
            server.sendmail(self.username, receiver_email, message)
            
    def sendpdf(self):
        subject = "An email with attachment incase of Emergency"
        body = "This is an email with attachment sent from a schedule by Example incase of emergency"
        sender_email = "example@gmail.com"
        receiver_email = "example@gmail.com"
        password = "MddjhXHy"

# Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
        message.attach(MIMEText(body, "plain"))

        filename = "document.pdf"  # In same directory as script

# Open PDF file in binary mode
        with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
            encoders.encode_base64(part)

# Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
                )

# Add attachment to message and convert message to string
            message.attach(part)
            text = message.as_string()

# Log in to server using secure context and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, text)


    
        #print(msg2['Date'])

ob=login()
#print(ob.last_sent())

#imap.logout()

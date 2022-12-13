# Import modules
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os, shutil

# Set up the email addresses and password. Please replace below with your email address and password
email_from = 'eugenewong@idgs.my'
password = 'gqqnimxdpusfedzo'
email_to = 'eugenewong@idgs.my'

# Create a MIMEMultipart class, and set up the From, To, Subject fields
email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['To'] = email_to
email_message['Subject'] = f'Netmon - Realtime Graph'


# Connect to the Gmail SMTP server and Send Email
try:
    print('Sending email...')
    #context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(email_from, password)
        server.sendmail(email_from, email_to, 'Hello')
    #deleteAllFiles(imagePath) 
    print('Email is sent')
except Exception as e:
    print("Sending Error:", e)

server.close()


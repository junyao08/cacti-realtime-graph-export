import smtplib, ssl
import imghdr
import os, shutil
from email.message import EmailMessage
import logging

#Create and configure logger
logging.basicConfig(filename="realtime_email.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object that
logger = logging.getLogger()

# Setting the threshold of logger to DEBUGGER
logger.setLevel(logging.DEBUG)

Sender_Email = "eugenewong@idgs.my"
Receiver_Email = "eugenewong@idgs.my"
#Bcc_Email = "tohseng@idgs.my"
# Password App from Google 
Password = "gqqnimxdpusfedzo"


newMessage = EmailMessage()                         
newMessage['Subject'] = "Netmon Cacti - Export Realtime Graph" 
newMessage['From'] = Sender_Email                   
newMessage['To'] = Receiver_Email
#newMessage['Bcc'] = Bcc_Email
newMessage.set_content('Realtime graph report')

message = "This is my message"
newMessage.set_content(message)

try:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(Sender_Email, Password)              
        smtp.send_message(newMessage)
    logger.debug('Email is sent. Deleting old realtime graph...')
except Exception as e:
    err = 'SMTP failed to send email: {}'.format(str(e))
    logger.error(err)


# Import modules
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
import os
import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
f_handler = logging.FileHandler('file.log')
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(f_handler)


# Define the HTML document
html = '''
    <html>
        <body>
            <h1>Realtime Graph Report</h1>        
        </body>
    </html>
    '''

# Function to attach files as MIMEApplication to the email
def attach_file_to_email(email_message, filename):
    # Open the attachment file for reading in binary mode, and make it a MIMEApplication class
    if filename.endswith('.png') or filename.endswith('.svg'):
        try:
            with open(filename, "rb") as f:
                img = MIMEImage(f.read())
                email_message.attach(img)
        except Exception as e:
            logger.error('Error sending png: ', e)

# Set up the email addresses and password. Please replace below with your email address and password
email_from = 'netmon.monash.edu.my@netmon.monash.edu.my'
email_to = 'eugenewong@idgs.my'
cc = ['james.chia@monash.edu', 'tinesh.ragindran@monash.edu', 'lim.teckyee@monash.edu']
bcc = ['tohseng@idgs.my', 'eugenewong@idgs.my']

smtp_server = 'localhost'
smtp_port = 587

# Create a MIMEMultipart class, and set up the From, To, Subject fields
email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['To'] = email_to
email_message['Subject'] = f'Netmon - Realtime Graph'
email_message['Cc'] = ', '.join(cc)
email_message['Bcc'] = ', '.join(bcc)

# Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
email_message.attach(MIMEText(html, "html"))

# Get the image path
#imagePath = "/home/netmon.monash.edu.my/public_html/cacti-1.2.20/cache/realtime/"
imagePath = '.'

# Attached PNG image to email
for image in os.listdir(imagePath):
    attach_file_to_email(email_message, image)
logger.error('Png files attached successfully')

# Convert it as a string
email_string = email_message.as_string()
logger.error('Convert it as a string')

# Connect to the Gmail SMTP server and Send Email
try:
    logger.error('Sending email...')
    # context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.ehlo()
        server.set_debuglevel(1)
        server.sendmail(email_from, email_to, email_string)
        server.close()
    logger.error('Email is sent')
except Exception as e:
    logger.error("Sending Error:", e)



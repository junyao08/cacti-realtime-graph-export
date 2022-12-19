# Import modules
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os, shutil
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
                file_attachment = MIMEApplication(f.read())
            # Add header/name to the attachments    
            file_attachment.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )
            # Attach the file to the message
            email_message.attach(file_attachment)
            print('File name: ', filename)
        except Exception as e:
            logger.error('Error sending png: ', e)


# Function to delete realtime graph that has been sent.
def deleteAllFiles(folderPath):
    for file in os.listdir(folderPath):
        # Grab only png files
        if file.endswith(".rrd") or file.endswith(".png"):
            file_path = os.path.join(folderPath, file)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                print('File removed: ', file)
            except Exception as e:
                logger.error('Failed to delete %s. Reason: %s' % (file_path, e))


# Set up the email addresses and password. Please replace below with your email address and password
email_from = 'eugenewong@idgs.my'
password = 'gqqnimxdpusfedzo'
email_to = 'eugenewong@idgs.my'

# Create a MIMEMultipart class, and set up the From, To, Subject fields
email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['To'] = email_to
email_message['Subject'] = f'Netmon - Realtime Graph'

# Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
email_message.attach(MIMEText(html, "html"))

# Get the image path
imagePath = "."

# Attached PNG image to email
for image in os.listdir(imagePath):
    attach_file_to_email(email_message, image)
logger.error('Png files attached successfully')

# Convert it as a string
email_string = email_message.as_string()
print('Convert it as a string')

# Connect to the Gmail SMTP server and Send Email
try:
    print('Sending email...')
    # context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, local_hostname=None, timeout=1200) as server:
        server.ehlo()
        server.set_debuglevel(1)
        server.login(email_from, password)
        server.sendmail(email_from, email_to, email_string)
        server.close()
        server.noop()
    deleteAllFiles(imagePath) 
    print('Email is sent')
except Exception as e:
    logger.error("Sending Error:", e)




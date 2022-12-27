# Import modules
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
import os, shutil
import logging
import time

# Create a logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Create a file handler
handler = logging.FileHandler('log.txt')
handler.setLevel(logging.DEBUG)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

abspath = os.path.abspath(os.path.dirname(__file__))
dname = os.path.dirname(abspath)
os.chdir(dname)
logger.debug(dname)

# Define the HTML document
html = '''
    <html>
        <body>
            <h1>Realtime Graph Report</h1>        
        </body>
    </html>
    '''

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
            except Exception as e:
                logger.error("Error while deleting files: ", str(e))

def rename_graph_name(folderpath, filename):
    image_path = os.path.join(folderpath, filename)
    if filename.endswith('.png') or filename.endswith('.svg'):
        if filename.endswith('514.png'):
            os.rename(image_path, folderpath + 'musc-cx2-sw1-time-500m-dia.png')
        elif filename.endswith('512.png'):
            os.rename(image_path, folderpath + 'musc-aims-sw1-maxis-500m-dia.png')
        elif filename.endswith('515.png'):
            os.rename(image_path, folderpath + 'musc-cx2-sw1-myix-1g-cx2.png')
        elif filename.endswith('513.png'):
            os.rename(image_path, folderpath +'musc-aims-sw-myix-1g-aims.png')
        elif filename.endswith('508.png'):
            os.rename(image_path, folderpath +'musc-9-5-gw1-myren-300m-ppl.png')
        elif filename.endswith('507.png'):
            os.rename(image_path, folderpath + 'musc-9-5-gw1-1g-pll-to-cx2.png')
        elif filename.endswith('510.png'):
            os.rename(image_path, folderpath + 'musc-2-0-gw1-1g-pll-to-aims.png')
        elif filename.endswith('523.png'):
            os.rename(image_path, folderpath + 'musc-vss-core-csjb-300m-pll.png')
        elif filename.endswith('1281.png'):
            os.rename(image_path, folderpath + 'musc-9-5-bds1-smp-100m-pll.png')

# Function to attach files as MIMEApplication to the email
def attach_file_to_email(email_message, filename):
    # Open the attachment file for reading in binary mode, and make it a MIMEApplication class
    if filename.endswith('.png') or filename.endswith('.svg'):
        try:
            with open(filename, "rb") as f:
                img = MIMEImage(f.read())
                email_message.attach(img)
                logger.debug("File attached: " + filename)
        except Exception as e:
            logger.error('Error sending png: ', str(e))

# Set up the email addresses and password. Please replace below with your email address and password
email_from = 'netmon.monash.edu.my@netmon.monash.edu.my'
#email_to = 'tinesh.ragindran@monash.edu, lim.teckyee@monash.edu, james.chia@monash.edu, tohseng@idgs.my, eugenewong@idgs.my'
email_to = 'eugenewong@idgs.my'

smtp_server = 'localhost'
smtp_port = 587

# Create a MIMEMultipart class, and set up the From, To, Subject fields
logger.debug('Creating the email message')
email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['To'] = email_to
email_message['Subject'] = f'Netmon - Realtime Graph'

# Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
email_message.attach(MIMEText(html, "html"))

# Get the image path
imagePath = "/home/netmon.monash.edu.my/public_html/cacti-1.2.20/cache/realtime/"

for image in os.listdir(imagePath):
    rename_graph_name(imagePath, image)
logger.debug("All files renamed")

# Attached PNG image to email
for image in os.listdir(imagePath):
    image_path = os.path.join(imagePath, image)
    attach_file_to_email(email_message, image_path)
logger.debug('Png files attached successfully')

# Convert it as a string
email_string = email_message.as_string()
logger.debug('Convert it as a string')

# Connect to the Gmail SMTP server and Send Email
try:
    logger.debug('Connecting to the SMTP server')
    # context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.set_debuglevel(1)
        logger.debug('Sending the email')
        start_time = time.time()
        server.sendmail(email_from, email_to.split(','), email_string)
        end_time = time.time()
        logger.debug(f'Email sent in {end_time - start_time:.2f} seconds')
        server.close()
        logger.debug('Disconnecting from the SMTP server')
except Exception as e:
    logger.error("Sending Error:", str(e))

#deleteAllFiles(imagePath)
#logger.debug('PNG deleted')
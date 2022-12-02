import smtplib
import imghdr
import os, shutil
from email.message import EmailMessage

Sender_Email = "eugenewong@idgs.my"
Receiver_Email = "eugenewong@idgs.my"
Bcc_Email = "tohseng@idgs.my"
# Password App from Google 
Password = "gqqnimxdpusfedzo"

def deleteAllFiles(folderPath):
    for file in os.listdir(folderPath):
        # Grab only png files
        if not file.endswith(".php") and file.endswith(".py") and file.endswith(".txt") and file.endswith('.htaccess'):
            file_path = os.path.join(folderPath, file)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

newMessage = EmailMessage()                         
newMessage['Subject'] = "Netmon Cacti - Export Realtime Graph" 
newMessage['From'] = Sender_Email                   
newMessage['To'] = Receiver_Email
newMessage['Bcc'] = Bcc_Email
newMessage.set_content('Realtime graph report') 

imagePath = "/home/netmon.monash.edu.my/public_html/cacti/cache/realtime/"
imagesDir = os.listdir(imagePath)
images = []

for image in imagesDir:
    if image.endswith(".png"):
        images.append(image)

for image in images:
    # Open image file in binary mode
    with open(image, "rb") as attachment:
        image_data = attachment.read()
        image_type = imghdr.what(attachment.name)
        image_name = attachment.name
    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Sender_Email, Password)              
    smtp.send_message(newMessage)

# Remove graph imgages after email to receipient.
deleteAllFiles(imagePath)


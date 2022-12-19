import smtplib
import imghdr
from email.message import EmailMessage
import os

# Set up the email addresses and password. Please replace below with your email address and password
Sender_Email = 'eugenewong@idgs.my'
Reciever_Email = 'eugenewong@idgs.my'
Password = 'gqqnimxdpusfedzo'

newMessage = EmailMessage()                         
newMessage['Subject'] = "Check out the new logo" 
newMessage['From'] = Sender_Email                   
newMessage['To'] = Reciever_Email                   
newMessage.set_content('Let me know what you think. Image attached!') 

# Get the image path
imagePath = "/home/netmon.monash.edu.my/public_html/cacti-1.2.20/cache/realtime/"

# Attached PNG image to email
for image in os.listdir(imagePath):
    if image.endswith(".png"):
        with open(image, 'rb') as f:
            image_data = f.read()
            image_type = imghdr.what(f.name)
            image_name = f.name
        newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Sender_Email, Password)              
    smtp.send_message(newMessage)
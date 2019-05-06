
import time

import os
import glob
import smtplib
import base64

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from email.mime.image import MIMEImage

from email.mime.multipart import MIMEMultipart
import subprocess
import sys
 
gmail_user = "anuja4skype@gmail.com"
gmail_pwd = "anuja4sy"
FROM = 'anuja4skype@gmail.com'
TO = ['anujanwatpade@gmail.com','leenawani@gmail.com'] #must be a list

 
time.sleep(1)
msg = MIMEMultipart()
time.sleep(1)
msg['Subject'] ="testing msg send from python"
time.sleep(1)


data=""

def sendMail():
    
    fp = open('image1.jpg','rb' )
    time.sleep(1)
    img = MIMEImage(fp.read())
    time.sleep(1)
    fp.close()
    time.sleep(1)
    msg.attach(img)
    time.sleep(1)
    try:
	server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
	print "smtp.gmail"
        server.ehlo()
	print "ehlo"
        server.starttls()
	print "starttls"
        server.login(gmail_user, gmail_pwd)
	print "reading mail & password"
        server.sendmail(FROM, TO, msg.as_string())
	print "from"
        server.close()
        print 'successfully sent the mail'

    except:
	print "failed to send mail"
	GPIO.output(25, False)


sendMail()



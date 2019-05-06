import RPi.GPIO as gpio
import picamera
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
msg['Subject'] ="Confidential Data Security Theft Alert"
time.sleep(1)

led=17
pir=18
HIGH=1
LOW=0
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(led, gpio.OUT)            # initialize GPIO Pin as outputs
gpio.setup(pir, gpio.IN)            # initialize GPIO Pin as input
data=""


def sendMail(data):
    data1='%s.jpg'%data
    fp = open(data1,'rb' )
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
        gpio.output(led, True)
        time.sleep(2)
        gpio.output(led, False)
        time.sleep(2)
    except:
	print "failed to send mail"
	gpio.output(led, False)

def capture_image():
    data= time.strftime("%d_%b_%Y|%H:%M:%S")
    camera.start_preview()
    time.sleep(5)
    print data
    camera.capture('%s.jpg'%data)
    camera.stop_preview()
    time.sleep(1)
    sendMail(data)

gpio.output(led ,False)
camera = picamera.PiCamera()
camera.rotation=180
camera.awb_mode= 'auto'
camera.brightness=55
while 1:
    if gpio.input(pir)==1:
        gpio.output(led, HIGH)
        capture_image()
	subprocess.Popen("python sms.py",shell = True).communicate()
        while(gpio.input(pir)==1):
            time.sleep(1)
        
    else:
        gpio.output(led, LOW)
        time.sleep(0.01)


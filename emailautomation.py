import random
import smtplib
from email.message import EmailMessage

def generate_otp():
    otp = random.randint(100000, 999999)
    return otp
def sending_mail(receiver, sender, password, otp):
    email = EmailMessage()
    email['To'] = receiver
    email['From'] = sender
    email['Subject'] = 'Your otp for verification'
    body = f"please enter your OTP when asked{otp}"
    email.set_content(body)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender,password)
    server.send_message(email)
    server.quit()
    print('OTP Sent')

def otp_verification(otp):
    votp = int(input('Enter the otp you received:'))
    if otp == votp:
        print('verification successful')
    else:
        print('verification unsuccessful')
otp = generate_otp()
receiver = input('please enter receiver mail id:')
sender = 'reddyvamshi7270@gmail.com'
password = 'kjto wlas yavk mtkk'
sending_mail(receiver,sender,password,otp)
otp_verification(otp)
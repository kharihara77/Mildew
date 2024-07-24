import smtplib
import base64
from email.mime.text import MIMEText
from email.message import EmailMessage

def sendEmail(mildex, date):
    from_email = "testingemail1473011@gmail.com"
    from_password = ""
    to_email = "hmahesh2@gmail.com"

    subject = " Mildex for " + date
    message = date + " Mildew Risk Index is " + str(mildex)

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email
    msg.set_content(message)

    try:
        gmail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        gmail.ehlo()
        gmail.login(from_email, from_password)
        gmail.send_message(msg)
        gmail.close()
        print("successfully send mail")
    except:
        print ("failed to send mail")

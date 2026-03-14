import smtplib

def send_email():

    sender = "your_email@gmail.com"
    receiver = "doctor@gmail.com"

    message = "Subject: Health Alert\n\nCritical anomaly detected"

    server = smtplib.SMTP("smtp.gmail.com",587)

    server.starttls()

    server.login(sender,"your_app_password")

    server.sendmail(sender,receiver,message)

    server.quit()
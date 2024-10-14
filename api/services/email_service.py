import os
from pathlib import Path
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import email

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

def send_token(message_to, token): 
    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = os.getenv('email')
        msg['To'] = message_to
        msg['Subject'] = "Cambio de Contraseña"
        body_text = ""
        body_html = f"Introduce el siguiente código de verificación para cambiar tu contraseña: {token}"
        part1 = MIMEText(body_text, 'plain')
        part2 = MIMEText(body_html, 'html')
        msg.attach(part1)
        msg.attach(part2)
        print(msg)
        smtp_uri='',
        if os.getenv('email_platform').lower() == 'gmail':
            smtp_uri='smtp.gmail.com'
        else:
            smtp_uri='smtp-mail.outlook.com'
        mail = smtplib.SMTP(smtp_uri, 587, timeout=20) ###587 old port               
        mail.ehlo()
        mail.starttls()
        mail.ehlo()        
        recipient = message_to.split(",")
        mail.login(os.getenv('email'), os.getenv('email_password'))
        mail.sendmail(os.getenv('email'), recipient, msg.as_string())        
        mail.quit()
        return 1
    except (Exception, KeyboardInterrupt) as e:
        print(e)
        return 0


def send_results(message_to,message,attachments):
    try:
        messageto=message_to
        msg = MIMEMultipart('alternative')

        msg['From'] = os.getenv('email')
        msg['To'] = messageto
        msg['Subject'] = "Resultados de Análisis"
        body_text = ""
        body_html = message

        part1 = MIMEText(body_text, 'plain')
        part2 = MIMEText(body_html, 'html')

        msg.attach(part1)
        msg.attach(part2)
        smtp_uri='',
        if os.getenv('email_platform').lower() == 'gmail':
            smtp_uri='smtp.gmail.com'
        else:
            smtp_uri='smtp-mail.outlook.com'
        mail = smtplib.SMTP(smtp_uri, 587, timeout=20)
        mail.ehlo()
        mail.starttls()
        mail.ehlo()        
        recipient = messageto.split(",")
        part = MIMEBase('application', "octet-stream")
        with open(attachments, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        attached=attachments
        part.add_header("Content-Disposition",f"attachment; filename= {attached}")
        msg.attach(part)
        mail.login(os.getenv('email'), os.getenv('email_password'))
        mail.sendmail(os.getenv('email'), recipient, msg.as_string())        
        mail.quit()
        return 1
    except (Exception, KeyboardInterrupt) as e:
        print(e)
        return 0
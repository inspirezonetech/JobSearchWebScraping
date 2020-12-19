import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from config import cfg


class Gmailer:
    def __init__(self, username, password, hostURL="smtp.gmail.com", secure=True):
        """
        Init Gmailer - default values are for Google servers

        Disable 2 step verification and allow `less secure apps` to access your google account (https://support.google.com/accounts/answer/6010255); you might need to display unlock Captcha if you still get an `SMTPAuthenticationError` error (https://accounts.google.com/DisplayUnlockCaptcha)

        Google restrictions: Free accounts are limited to 500 emails per day and are rate-limited to about 20 emails per second
        Google Ports: 465 (SSL) oder 587 (TLS/STARTTLS)

        :param hostURL: URL of the SMTP server
        :param secure: use SSL (True) or not (secure is of type bool)
        """
        self.SSL = secure
        self.hostURL = hostURL

        if self.SSL is True:
            SCout.info("Using secure (SSL) connection...")
            self.SMTPport = 465
            self.server = smtplib.SMTP_SSL(host=self.hostURL, port=self.SMTPport)
            self.server.ehlo()
            self.server.login(username, password)
        else:
            
            SCout.info("Using non-secure (unencrypted) connection...")
            self.SMTPport = 465
            self.server = smtplib.SMTP(host=self.hostURL, port=self.SMTPport)
            self.server.ehlo()

    def send(self, FROM, TO, SUBJECT, BODY ,FILE_PATH):
    	"""
    	FROM: email of the sender
    	TO: list of receiver emails
    	SUBJECT: subject of the email
    	BODY: body of the email
    	FILE_PATH: path of the file to be sent. 
    	"""

        
        msg = email.MIMEMultipart.MIMEMultipart()
        msg.add_header("From", FROM)
        msg.add_header("To", ", ".join(TO))
        msg.add_header("Subject", SUBJECT)
        
        if BODY is not None:
            if isinstance(BODY, tuple):
                msg.attach(email.mime.Text.MIMEText(*BODY))
            elif isinstance(BODY, str):
                msg.attach(email.mime.Text.MIMEText(BODY))
            else:
                raise TypeError()
        
        if FILE_PATH is not None:
            fb = open(FILE_PATH, "rb")
            att = email.mime.application.MIMEApplication(fb.read())
            fb.close()
            att.add_header("Content-Disposition", "attachment;filename=%s" % os.path.basename(FILE_PATH))
            msg.attach(att)
		
		try:
            self.server.sendmail(FROM, TO, msg.as_string())
            SCout.info("Email sent!")
        except:
            SCout.error("Email not sent - something went wrong...")

    def closeConnection(self):
        self.server.close()

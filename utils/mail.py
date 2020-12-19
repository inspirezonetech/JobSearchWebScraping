import os
import smtplib
import logging
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Gmailer:
    """Gmailer class"""

    def __init__(self, username, password, hosturl="smtp.gmail.com", secure=True):
        """Init Gmailer - default values are for Google servers
            Disable 2 step verification and allow `less secure apps` to access your google account (https://support.google.com/accounts/answer/6010255); you might need to display unlock Captcha if you still get an `SMTPAuthenticationError` error (https://accounts.google.com/DisplayUnlockCaptcha)
            Google restrictions: Free accounts are limited to 500 emails per day and are rate-limited to about 20 emails per second
            Google Ports: 465 (SSL) oder 587 (TLS/STARTTLS)
            :param hostURL: URL of the SMTP server
            :param secure: use SSL (True) or not (secure is of type bool)
        """

        self.SSL = secure
        self.hostURL = hosturl

        if self.SSL is True:
            logging.info("Using secure (SSL) connection...")
            self.SMTPport = 465
            self.server = smtplib.SMTP_SSL(host=self.hostURL, port=self.SMTPport)
            self.server.ehlo()
            self.server.login(username, password)
        else:

            logging.info("Using non-secure (unencrypted) connection...")
            self.SMTPport = 465
            self.server = smtplib.SMTP(host=self.hostURL, port=self.SMTPport)
            self.server.ehlo()

    def send(self, sender, receiver, subject, body, file_path):
        """FROM: email of the sender
            TO: list of receiver emails
            SUBJECT: subject of the email
            BODY: body of the email
            FILE_PATH: path of the file to be sent."""

        msg = MIMEMultipart.MIMEMultipart()
        msg.add_header("From", sender)
        msg.add_header("To", ", ".join(receiver))
        msg.add_header("Subject", subject)

        if body is not None:
            if isinstance(body, tuple):
                msg.attach(MIMEText(*body))
            elif isinstance(body, str):
                msg.attach(MIMEText(body))
            else:
                raise TypeError()

        if file_path is not None:
            fb = open(file_path, "rb")
            att = MIMEApplication(fb.read())
            fb.close()
            att.add_header("Content-Disposition", "attachment;filename=%s" % os.path.basename(file_path))
            msg.attach(att)
        try:
            self.server.sendmail(sender, receiver, msg.as_string())
            logging.info("Email sent!")
        except Exception as e:
            logging.error("Email not sent - something went wrong...", exc_info=e)

    def closeConnection(self):
        """
        Closes SMTP server
        """
        self.server.close()

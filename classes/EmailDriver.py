import smtplib
from email.message import EmailMessage

from classes.envManager import EnvManager

class EmailDriver():

    smtp_server = 'SMTP_SERVER'
    smtp_port = 'SMTP_PORT'
    user_name = 'EMAIL'
    password = 'PASSWORD'
    from_address = ''

    def __init__(self):
        self.set_validation_fields()

    def set_validation_fields(self):
        envManager = EnvManager()
        self.smtp_server = envManager.get_from_env(self.smtp_server)
        self.smtp_port = int(envManager.get_from_env(self.smtp_port))
        self.user_name = envManager.get_from_env(self.user_name)
        self.password = envManager.get_from_env(self.password)
        self.from_address = envManager.get_from_env(self.from_address)
        print(self.from_address, self.user_name, self.password, self.smtp_server, self.smtp_port)


    def send_simple_email(self, to, subject, body):
        message = self.get_message_obj(to, subject, body)
        s = self.get_smtp_handler()
        s.send_message(message)

    def get_smtp_handler(self):
        s = smtplib.SMTP(host=self.smtp_server, port=self.smtp_port)
        s.starttls()
        s.login(self.user_name, self.password)
        return s

    def get_message_obj(self, to, subject, body):
        message = EmailMessage()
        message['To'] = to
        message['Subject'] = subject
        message['From'] = self.get_from_address()
        message.set_content(body)
        return message

    def get_from_address(self):
        return self.from_address if self.from_address else self.user_name


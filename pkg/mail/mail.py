import asyncio
import os
import smtplib
from concurrent.futures import ThreadPoolExecutor
from email.message import EmailMessage
from fastapi.logger import logger


class MailConfig:
    smtp_server: str = os.getenv("SMTP")
    smtp_port: int = os.getenv("PORT")
    sender_email: str = os.getenv("EMAIL")
    sender_password: str = os.getenv("PASSWORD")


class SendSender(MailConfig):

    async def send_message(self, to: str, subject: str, messages: str):
        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor() as executor:
            await loop.run_in_executor(executor, self._send_message, to, messages, subject)

    def _send_message(self, subject, messages, to):
        message = EmailMessage()
        message['From'] = MailConfig.sender_email
        message['To'] = to
        message['Subject'] = subject
        message.set_content(messages, charset="utf-8")

        try:
            server = smtplib.SMTP(MailConfig.smtp_server, MailConfig.smtp_port)
            server.starttls()
            server.login(MailConfig.sender_email, MailConfig.sender_password)
            server.send_message(message)
            server.quit()
            logger.info('Письмо успешно отправлено')

        except Exception as e:
            logger.fatal(f'Произошла ошибка: {str(e)}')


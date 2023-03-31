import time
import os
import smtplib
import mimetypes
from tqdm import tqdm
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import datetime


def send_email():
    time.sleep(2)
    sender = "nya.prog.bot@gmail.com"
    password = "eduniicggbqbfyrq"
    getter = "kostya111000@gmail.com"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    times = datetime.today()

    server.login(sender, password)
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = getter
    msg["Subject"] = f"Парсинг наличия и стоимости {times}"

    for file in tqdm(os.listdir("attachments")):
        time.sleep(0.4)
        filename = os.path.basename(file)
        ftype, encoding = mimetypes.guess_type(file)
        file_type, subtype = ftype.split("/")

        with open(f"attachments/{file}", "rb") as f:
            file = MIMEApplication(f.read(), subtype)

        file.add_header('content-disposition', 'attachment', filename=filename)
        msg.attach(file)
    server.sendmail(sender, getter, msg.as_string())
    print(f'[!] Письмо отправлено')
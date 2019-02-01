from django.conf import settings
import smtplib
from email.mime.text import MIMEText

def send_mails(address):
    print(str(address) + " 으로 발송중입니다.")
    id = settings.CONF_FILE['email']['id']
    pw = settings.CONF_FILE['email']['pw']
    msg = address
    msg = MIMEText(address)
    msg['Subject'] = str(address) + '새로운 게시물이 등록되었습니다.'
    msg['To'] = address
    msg['From'] = id
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(id, pw)
    s.sendmail(id, address, msg.as_string())
    s.quit()
    print(str(address) + " 메일이 발송되었습니다.")

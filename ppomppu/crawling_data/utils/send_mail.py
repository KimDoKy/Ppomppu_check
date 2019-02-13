from django.conf import settings
import smtplib
from email.mime.text import MIMEText

def send_mails(address, keyword, detail_link):
    id = settings.CONF_FILES['email']['id']
    pw = settings.CONF_FILES['email']['password']
    msg = '키워드 ' + keyword + ' 게시물이 새로 등록되었습니다. <br/>' + detail_link
    msg = MIMEText(msg)
    msg['Subject'] = keyword + ' 새로운 게시물이 등록되었습니다.' 
    msg['To'] = address
    msg['From'] = "뽐뿌 게시판"
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(id, pw)
    s.sendmail(id, address, msg.as_string())
    s.quit()

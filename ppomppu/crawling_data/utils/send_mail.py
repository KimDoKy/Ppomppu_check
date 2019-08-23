from django.conf import settings
import smtplib
from email.mime.text import MIMEText

def send_mails(key, instance):
    address = str(key.owner)
    keyword = key.keyword
    detail_link = instance['detail_link']
    prod_img = instance['prod_image']
    title = instance['title']
    id = settings.CONF_FILES['email']['id']
    pw = settings.CONF_FILES['email']['password']
    body = '''
        <center>
        <h3>[뽐뿌 Checker]</h3>
        <br>
        지정한 키워드: <b><a href="{0}">{1}</b></a>
        게시물이 새로 등록되었습니다.
        <br><br>
        <a href="{0}">{2}</a>
        <img src="http://{3}">
        <br><br>
        <hr>
        <a href="https://app.pycon.shop"><img src="https://app.pycon.shop/img/logo.135e5f07.png" width=100px></a>
        </center>
        '''.format(detail_link, keyword, title, prod_img)
    msg = MIMEText(body, 'html')
    msg['Subject'] = '[뽐뿌 Checker] ' +  keyword + ' 새로운 게시물이 등록되었습니다.'
    msg['To'] = address
    msg['From'] = "뽐뿌 Checker"
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(id, pw)
    s.sendmail(id, address, msg.as_string())
    s.quit()

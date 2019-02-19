import re
from .send_mail import send_mails

def matching_keyword(keywords, new_data):
    # 유저가 등록한 키워드와 업데이트된 타이틀을 비교한다.
    # 비교후 일치하면 안내메일을 발송한다.
    for key in keywords:
        if re.search(key.keyword, new_data['title']):
            send_mails(key, new_data)
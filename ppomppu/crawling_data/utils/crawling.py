import requests
from bs4 import BeautifulSoup as bs
import re

def craw_item(url):
    html = requests.get(url)
    contents = {}
    re_img = re.compile('^[a-z0-9./_]+') # 이미지 링크를 뽑아내기 위한 정규식
    re_src = re.compile('[^?]+$')        # 상세 링크를 뽑아내기 위한 정규식
    try:
        if html.status_code == 200:
            html = html.text
            soup = bs(html, 'html.parser')
            items = soup.find_all('tr', {'align':'center'})
            for index in range(len(items)):
                if index == 0 or index == 1: continue # menu(0), 공지(1)은 제외
                title = items[index].find('font').text
                category = items[index].find('nobr').text
                write_date = items[index].find('nobr',{'class':'eng'}).text
                link = items[index].find('td',{'valign':'middle'})
                href_url = link.find('a')['href']
                detail_url = re_src.findall(href_url)
                detail_link = 'http://www.ppomppu.co.kr/zboard/view.php?' + detail_url[0]
                image_url = re_img.match(items[index].find('img')['src'][2:])
                image = image_url.group()
                contents['content_' + str(index)] = {'title':title,
                                                  'category':category,
                                                  'write_date':write_date,
                                                  'detail_link':detail_link,
                                                  'prod_image':image}
        return contents
    except Exception as e:
        print('크롤링되지 않았습니다.', '\n error message: ', e)

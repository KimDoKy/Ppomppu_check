import requests
from bs4 import BeautifulSoup as bs

def craw_item(url):
    html = requests.get(url)
    contents = {}
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
                detail_url = link.find('a')['href'][12:]
                detail_link = 'http://www.ppomppu.co.kr/zboard/view.php?id=' + detail_url
                image = items[index].find('img')['src'][2:]
                contents['content_' + str(index)] = {'title':title,
                                                  'category':category,
                                                  'write_date':write_date,
                                                  'detail_link':detail_link,
                                                  'prod_image':image}
        return contents
    except Exception as e:
        print('크롤링되지 않았습니다.', '\n error message: ', e)

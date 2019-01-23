# coding: utf-8
import requests
from bs4 import BeautifulSoup as bs
import re

default_url = 'http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page='
detail_url = 'http://www.ppomppu.co.kr/zboard/view.php?id='

page_num = 5 # 하루 평균 게시판 4페이지 정도 올라옴

keyword = input('키워드를 입력하세요. ')

def craw_item(url):
    html = requests.get(url)
    print(html.status_code)
    html = html.text
    soup = bs(html, 'html.parser')
    items = soup.find_all('tr', {'align':'center'})
    for num, item in enumerate(items):
        # menu, 공지사항 제외
        if num == 0 or num == 1: continue
        elif re.search(keyword, item.find('font').text) == None: continue 
        print('----------', str(num), '----------')
        print('category: ', item.find('nobr').text)
        print('title: ', item.find('font').text)
        link = item.find('td',{'valign':'middle'})
        print('detail_link: ', detail_url + link.find('a')['href'][12:])
        print('image: ', item.find('img')['src'][2:])
        print('create_at: ', item.find('nobr',{'class':'eng'}).text)

for i in range(1, page_num):
    url = default_url + str(i)
    print(url)
    craw_item(url)

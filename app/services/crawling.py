import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
from datetime import datetime
import pandas as pd
import os
from collections import defaultdict


def crawling_article(query, news_num=5):
    date = str(datetime.now()) 
    date = date[:date.rfind(':')].replace(' ', '_') 
    date = date.replace(':','시') + '분' 

    #query = input('검색 키워드를 입력하세요 : ') 
    query = query.replace(' ', '+') 

    news_num = news_num #int(input('총 필요한 뉴스기사 수를 입력해주세요(숫자만 입력) : ')) 

    news_url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}'

    req = requests.get(news_url.format(query))
    soup = BeautifulSoup(req.text, 'html.parser')

    news_dict = defaultdict(list)
    idx = 0 
    cur_page = 1

    print()
    print('크롤링 중...')

    while idx < news_num:
    ### 네이버 뉴스 웹페이지 구성이 바뀌어 태그명, class 속성 값 등을 수정함(20210126) ###
        
        table = soup.find('ul',{'class' : 'list_news'})
        li_list = table.find_all('li', {'id': re.compile('sp_nws.*')})
        area_list = [li.find('div', {'class' : 'news_area'}) for li in li_list]
        a_list = [area.find('a', {'class' : 'news_tit'}) for area in area_list]
        
        for n in a_list[:min(len(a_list), news_num-idx)]:
            news_dict['title'].append(n.get('title'))
            news_dict['url'].append(n.get('href'))
            news_dict['query'].append(query)
            #  = {'title' : n.get('title'),
            #                 'url' : n.get('href') }
            idx += 1

        cur_page += 1
        
        pages = soup.find('div', {'class' : 'sc_page_inner'})
        next_page_url = [p for p in pages.find_all('a') if p.text == str(cur_page)][0].get('href')
        
        req = requests.get('https://search.naver.com/search.naver' + next_page_url)
        soup = BeautifulSoup(req.text, 'html.parser')

    print('크롤링 완료')

    print('데이터프레임 변환')
    news_df = pd.DataFrame(news_dict)

    return news_df



# df = crawling_article('백신예약')

# from sqlalchemy import create_engine
# engine = create_engine('postgresql://wxmedoqx:hihfM0QF3AtbKXRC8cOy_Nc5yVxrL_1j@arjuna.db.elephantsql.com/wxmedoqx')

# df.to_sql('Data', engine, if_exists='append')
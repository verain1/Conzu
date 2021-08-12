import requests
from bs4 import BeautifulSoup
from pytrends.request import TrendReq
import pandas as pd

news_site_url = 'https://www.thehindu.com/' #search/?q=xyz%20&order=DESC&sort=publishdate
headers  ={"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}



pytrend = TrendReq()

def get_top_keywords(country_name):
    trending = pytrend.trending_searches(pn=country_name)
    return list(trending[0])



trending_keywords = get_top_keywords('india')
#trending_keywords = ['Jennifer Aniston']

data = []
for kw in trending_keywords:
  #  print(kw)
    url = news_site_url + 'search/?q=' +kw +'%20&order=DESC&sort=publishdate'
    response = requests.get(url,headers=headers)
   # print(response)
    soup = BeautifulSoup(response.content,'lxml')
    try:
        result = soup.find_all('div',class_='story-card-news')[:2]
        
    except:
        pass
    for each in result:
        #print(each)
        a_tag = each.find('a',href=True,class_='story-card75x1-text')
        title = a_tag.text
        link = a_tag['href'][25:]
        data.append({'title':title,'source':'The Hindu','link':news_site_url+'/'+link})



df = pd.DataFrame(data)

def get_th_data(as_df=False):
    if as_df:
        return df
    return data
print(df['link'][0])
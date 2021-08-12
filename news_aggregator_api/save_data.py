from ndtv_scraper import get_ndtv_data # ndtv scraper
from toi_scraper import get_toi_data # toi scraper
from the_hindu_scraper import get_th_data
import pandas as pd
import os

data1 = get_ndtv_data() 
data2 = get_toi_data()
data3 = get_th_data()
data = data1 + data2 + data3

data = pd.DataFrame(data)
os.system('cd ..')
data.to_csv('articles.csv')



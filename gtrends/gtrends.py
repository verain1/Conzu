from pytrends.request import TrendReq
import pandas as pd



pytrend = TrendReq()

def get_top_keywords(country_name):
    trending = pytrend.trending_searches(pn=country_name)
    return list(trending[0])




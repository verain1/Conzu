import pandas as pd

def articles_from_csv():

    #d = pd.read_csv('C:/news_1/news_aggregator/articles.csv')
    d = pd.read_csv('C:/news_1/news_aggregator/articles.csv')
    d = d.to_dict('records')
    return d
    

import pandas as pd

def articles_from_csv():

    d = pd.read_csv('articles.csv')
    d = d.to_dict('records')
    return d

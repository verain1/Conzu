from django.shortcuts import render
from news_aggregator_api.ndtv_scraper import get_ndtv_data # ndtv scraper
from news_aggregator_api.toi_scraper import get_toi_data # toi scraper

# Create your views here.




def show_news(request):
    '''line 16 and 17
    return a list of dcitionaries 
    each dictionary has a link to the article,source(ex. NDTV) and title
    check template for reference
    '''
    data1 = get_ndtv_data() 
    data2 = get_toi_data()
    data = data1 + data2 
    return render(request,'show_news/show_ndtv.html',{"data":data})

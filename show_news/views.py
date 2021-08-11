from django.shortcuts import render
from news_aggregator_api.ndtv_scraper import get_ndtv_data
from news_aggregator_api.toi_scraper import get_toi_data

# Create your views here.




def show_news(request):
    data1 = get_ndtv_data()
    data2 = get_toi_data()
    data = data1 + data2
    return render(request,'show_news/show_ndtv.html',{"data":data})

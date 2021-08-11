from django.shortcuts import render
from news_aggregator_api.ndtv_scraper import get_data

# Create your views here.




def show_news(request):
    data = get_data()
    return render(request,'show_news/show_ndtv.html',{"data":data})

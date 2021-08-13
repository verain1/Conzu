from django.shortcuts import render
from news_aggregator_api.get_articles import articles_from_csv
# Create your views here.




def show_news(request):
    data = articles_from_csv(filtered=True) # to be fixed
    return render(request,'show_news/show_news.html',{"data":data})

from django.shortcuts import render
from .models import Article
import requests
from bs4 import BeautifulSoup as BS
import random
# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('date')[:3]
    for art in articles:
        count = 0
        for i in range(len(art.text)):
            if art.text[i] == ' ':
                count+=1
            if count == 50:
                art.text = art.text[0:i] + "..."
                break
    req = requests.get('https://yandex.by/')
    html = BS(req.content, 'html.parser')
   
    return render(request, "index.html", {"articles":articles})


def article(request, articleId):
    art = Article.objects.get(id = articleId)
    print(art.id)
    return render(request, "article.html", {"art":art})

def test(request):
    return render(request, "base.html")


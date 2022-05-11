from django.shortcuts import render

from news.models import Articles


def index(request):
    news_top = Articles.objects.all().order_by("-date")[:3]

    data = {
        'title': 'My Blog',
        'news': news_top
    }
    return render(request, 'main/index.html', data)


def about(request):
    data = {
        'title': 'About Us'
    }
    return render(request, 'main/about.html', data)


def contact(request):
    data = {
        'title': 'Contact'
    }
    return render(request, 'main/contact.html', data)

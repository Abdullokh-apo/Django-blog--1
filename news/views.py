from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .forms import ArticlesForm
from .models import Articles


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/blog.html', {'news': news})


def work(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/news/#fh5co-blog')
        else:
            error = 'Не правильно заполнена'

    form = ArticlesForm()
    data = {
        'title': 'Work',
        'form': form,
        'error': error,
    }
    return render(request, 'news/work.html', data)


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

from datetime import datetime, timedelta
from random import randint

from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_http_methods, require_GET
from django.views.generic import TemplateView


@require_http_methods(['GET', 'POST'])
def index_page(request):
    return render(request, 'homepage/index.html')


class IndexPageView(TemplateView):

    template_name = 'homepage/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ArticleView(TemplateView):

    template_name = 'homepage/articles.html'

    def get_dates_list(self, count=10):
        result = []
        today = datetime.today()
        for i in range(count):
            date = today - timedelta(days=i)
            for j in range(randint(1, 4)):
                result.append(date.replace(hour=randint(0, 23)))
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = MyClass()
        obj.data = {'spam': 'eggs'}
        obj.list = list(range(10, 20))
        args = {
            'articles': list(range(1, 3)),
            'val1': '<h3>Value 1</h3>',
            'val2': '<h4>Value 2</h4>',
            'obj': obj,
            'dates': self.get_dates_list(),
            'num_cherries': 13,
        }
        context.update(args)
        return context


def article_year(request, year):
    return HttpResponse(f'<h1>Year is {year}</h1>')


class MyClass:
    foo = 42

from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET


@require_http_methods(['GET', 'POST'])
def index_page(request):
    return render(request, 'homepage/index.html')


@require_GET
def articles(request):
    args = {
        'articles': list(range(1, 8)),
        'val1': '<h3>Value 1</h3>',
        'val2': '<h4>Value 2</h4>',
    }
    return render(request, 'homepage/articles.html', args)

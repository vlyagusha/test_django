"""test_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, register_converter

from . import views

app_name = 'homepage'


class YearConverter:
    regex = r'[0-9]{4}'

    def to_python(self, value):
        value = int(value)
        if value < 2000:
            raise ValueError
        return value

    def to_url(self, value):
        return '%o4d' % value


register_converter(YearConverter, 'year')

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index'),
    path('articles/', views.ArticleView.as_view(), name='articles'),
    path('articles/<year:year>/', views.article_year, name='article_year'),
    # re_path(r'^articles/(?P<year>[0-9]{4})/$', views.article_year, name='articles'),
]

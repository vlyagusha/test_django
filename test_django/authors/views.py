from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Author


class IndexView(ListView):
    template_name = 'authors/index.html'
    model = Author
    context_object_name = 'authors'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['authors'] = Author.objects.all()
    #     return context

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)
        queryset = queryset.filter(id__gt=1)
        print(queryset)
        return queryset

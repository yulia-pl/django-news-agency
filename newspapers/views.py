from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import Newspaper

# Список газет
class NewspaperListView(ListView):
    model = Newspaper
    template_name = 'newspapers/newspaper_list.html'
    context_object_name = 'newspapers'

# Деталі газети
class NewspaperDetailView(DetailView):
    model = Newspaper
    template_name = 'newspapers/newspaper_detail.html'
    context_object_name = 'newspaper'

# Створення нової газети
class NewspaperCreateView(CreateView):
    model = Newspaper
    fields = ['title', 'content', 'published_date', 'topic', 'publishers']
    template_name = 'newspapers/newspaper_form.html'
    success_url = reverse_lazy('newspaper-list')

# Головна сторінка
class HomeView(TemplateView):
    template_name = 'home.html'

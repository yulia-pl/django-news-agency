from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views.generic import TemplateView
from .models import Newspaper

class NewspaperListView(ListView):
    model = Newspaper
    template_name = 'newspapers/newspaper_list.html'

class NewspaperDetailView(DetailView):
    model = Newspaper
    template_name = 'newspapers/newspaper_detail.html'

class NewspaperCreateView(CreateView):
    model = Newspaper
    fields = ['title', 'content', 'published_date', 'topic', 'publishers']
    template_name = 'newspapers/newspaper_form.html'

class HomeView(TemplateView):
    template_name = 'home.html'
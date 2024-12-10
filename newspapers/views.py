from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import Newspaper

class NewspaperListView(ListView):
    model = Newspaper
    template_name = 'newspapers/newspaper_list.html'
    context_object_name = 'newspapers'

    def get_queryset(self):
        return super().get_queryset().select_related('topic').prefetch_related('publishers')


class NewspaperDetailView(DetailView):
    model = Newspaper
    template_name = 'newspapers/newspaper_detail.html'
    context_object_name = 'newspaper'

    def get_queryset(self):
        return super().get_queryset().select_related('topic').prefetch_related('publishers')


class NewspaperCreateView(CreateView):
    model = Newspaper
    fields = ['title', 'content', 'published_date', 'topic', 'publishers']
    template_name = 'newspapers/newspaper_form.html'
    success_url = reverse_lazy('newspaper-list')


class HomeView(TemplateView):
    template_name = 'home.html'

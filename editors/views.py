from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Redactor
from django.urls import reverse_lazy

class RedactorListView(ListView):
    model = Redactor
    template_name = 'editors/redactor_list.html'
    context_object_name = 'redactors'

    def get_queryset(self):
        return super().get_queryset()


class RedactorDetailView(DetailView):
    model = Redactor
    template_name = 'editors/redactor_detail.html'
    context_object_name = 'redactor'

    def get_queryset(self):
        return super().get_queryset()


class RedactorCreateView(CreateView):
    model = Redactor
    fields = ['username', 'first_name', 'last_name', 'years_of_experience']
    template_name = 'editors/redactor_form.html'
    success_url = reverse_lazy('redactor-list')


class RedactorUpdateView(UpdateView):
    model = Redactor
    fields = ['username', 'first_name', 'last_name', 'years_of_experience']
    template_name = 'editors/redactor_form.html'

    def get_success_url(self):
        return reverse_lazy('redactor-list')

from django.views.generic import ListView, DetailView
from .models import Redactor

class RedactorListView(ListView):
    model = Redactor
    template_name = 'editors/redactor_list.html'

class RedactorDetailView(DetailView):
    model = Redactor
    template_name = 'editors/redactor_detail.html'

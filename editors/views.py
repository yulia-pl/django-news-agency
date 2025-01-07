from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Redactor

from django.urls import reverse_lazy


# List of Redactors
class RedactorListView(ListView):
    model = Redactor
    template_name = "editors/redactor_list.html"
    context_object_name = "redactors"

    def get_queryset(self):
        # Return the queryset of Redactors
        return super().get_queryset()


# Detailed view of a Redactor
class RedactorDetailView(DetailView):
    model = Redactor
    template_name = "editors/redactor_detail.html"
    context_object_name = "redactor"

    def get_queryset(self):
        # Return the queryset of Redactors
        return super().get_queryset()


# Create a new Redactor
class RedactorCreateView(CreateView):
    model = Redactor
    fields = ["username", "first_name", "last_name", "years_of_experience"]
    template_name = "editors/redactor_form.html"
    success_url = reverse_lazy("redactor-list")


# Update an existing Redactor
class RedactorUpdateView(UpdateView):
    model = Redactor
    fields = ["username", "first_name", "last_name", "years_of_experience"]
    template_name = "editors/redactor_form.html"

    def get_success_url(self):
        # Redirect to the list of Redactors after successful update
        return reverse_lazy("redactor-list")

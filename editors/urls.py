from django.urls import path

from . import views


urlpatterns = [
    # Redactor list view
    path("redactors/", views.RedactorListView.as_view(), name="redactor-list"),

    # Redactor detail view
    path("redactors/<int:pk>/", views.RedactorDetailView.as_view(), name="redactor-detail"),

    # Redactor create view
    path("redactors/create/", views.RedactorCreateView.as_view(), name="redactor-create"),

    # Redactor edit view
    path("redactors/<int:pk>/edit/", views.RedactorUpdateView.as_view(),
         name="redactor-edit"),
]

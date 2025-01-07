from django.urls import path

from . import views

urlpatterns = [
    # Newspaper list view
    path("", views.NewspaperListView.as_view(), name="newspaper-list"),

    # Newspaper detail view
    path("newspapers/<int:pk>/", views.NewspaperDetailView.as_view(),
         name="newspaper-detail"),

    # Newspaper create view
    path("newspapers/create/", views.NewspaperCreateView.as_view(),
         name="newspaper-create"),

    # Home page view
    path("home/", views.HomeView.as_view(), name="home"),
]

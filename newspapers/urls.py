from django.urls import path
from . import views

urlpatterns = [
    # Список газет
    path('', views.NewspaperListView.as_view(), name='newspaper-list'),

    # Деталі газети
    path('newspapers/<int:pk>/', views.NewspaperDetailView.as_view(), name='newspaper-detail'),

    # Створення нової газети
    path('newspapers/create/', views.NewspaperCreateView.as_view(), name='newspaper-create'),

    # Головна сторінка
    path('home/', views.HomeView.as_view(), name='home'),
]

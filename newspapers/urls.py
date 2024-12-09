from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewspaperListView.as_view(), name='newspaper-list'),
    path('<int:pk>/', views.NewspaperDetailView.as_view(), name='newspaper-detail'),
    path('create/', views.NewspaperCreateView.as_view(), name='newspaper-create'),
]

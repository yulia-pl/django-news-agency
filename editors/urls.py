from django.urls import path
from . import views

urlpatterns = [
    path('', views.RedactorListView.as_view(), name='redactor-list'),
    path('<int:pk>/', views.RedactorDetailView.as_view(), name='redactor-detail'),
]

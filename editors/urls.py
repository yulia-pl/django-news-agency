from django.urls import path
from . import views

urlpatterns = [
    # Список редакторів
    path('redactors/', views.RedactorListView.as_view(), name='redactor-list'),

    # Деталі редактора
    path('redactors/<int:pk>/', views.RedactorDetailView.as_view(), name='redactor-detail'),

    # Створення нового редактора
    path('redactors/create/', views.RedactorCreateView.as_view(), name='redactor-create'),

    # Редагування редактора
    path('redactors/<int:pk>/edit/', views.RedactorUpdateView.as_view(), name='redactor-edit'),
]

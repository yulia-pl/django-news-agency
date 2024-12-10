from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.AccountLoginView.as_view(), name='login'),
    path('logout/', views.AccountLogoutView.as_view(), name='logout'),
    path('register/', views.AccountRegisterView.as_view(), name='register'),
    path('profiles/', views.AccountDetailView.as_view(), name='profile'),  # Changed to plural
    path('profiles/edit/', views.AccountUpdateView.as_view(), name='edit_profile'),  # Changed to plural
]

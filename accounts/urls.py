from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.AccountLoginView.as_view(), name='login'),


    path('logout/', views.AccountLogoutView.as_view(), name='logout'),


    path('register/', views.AccountRegisterView.as_view(), name='register'),


    path('profile/', views.AccountDetailView.as_view(), name='profile'),


    path('profile/edit/', views.AccountUpdateView.as_view(), name='edit_profile'),
]

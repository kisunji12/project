from django.urls import path
from . import views as account_view
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', account_view.register, name='register'),
    path('profile/', account_view.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),


]

from django.contrib import admin
from django.urls import path, include
from .views import user_login, user_register, home

urlpatterns = [
    path('home/', home, name='home'),
    path('register/', user_register, name='user-register'),
    path('login/', user_login, name='user-login'),
    # path('accounts/', include('accounts.urls')),
]
from django.urls import path     
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup_page, name='signup-page'),
    path('login/', views.signin_page, name='signin-page'),
]

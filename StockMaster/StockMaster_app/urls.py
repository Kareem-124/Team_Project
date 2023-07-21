from django.urls import path     
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup_page, name='signup-page'),
    path('login/', views.signin_page, name='signin-page'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/profile', views.profile, name='profile'),
    path('dashboard/products', views.products, name='products-page'),
    path('register', views.register, name='registrProcess'),
    path('loging', views.login, name="loginProcess"),
    


]

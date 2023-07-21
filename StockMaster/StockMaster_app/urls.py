from django.urls import path     
from . import views
app_name = 'SM_app'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup_page, name='signup-page'),
    path('login/', views.signin_page, name='signin-page'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/profile', views.profile, name='profile'),
    path('dashboard/products', views.products, name='products-page'),
    path('register', views.register, name='registrProcess'),
    path('loging', views.login, name="loginProcess"),
<<<<<<< HEAD
=======
    path('order_page', views.order_page, name="order_page")
>>>>>>> 6037bc93c413806d741a560406d8132fc19331e6
    


]

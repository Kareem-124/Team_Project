from django.urls import path     
from . import views
app_name = 'SM_app'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup_page, name='signup-page'),
    path('login/', views.signin_page, name='signin-page'),
    path('register', views.register, name='registrProcess'),
    path('loging', views.login, name="loginProcess"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/profile', views.profile, name='profile'),
    path('products', views.products),
    path('register', views.register, name='registrProcess'),
    path('loging', views.login, name="loginProcess"),
    path('order_page', views.order_page, name='displayOrderPage'),
    path('dashboard/products/add_new', views.add_prodcut, name='add_product'),
    path('save_product/', views.save_product, name='save_product'),
    path('save_products/', views.save_products),
    path('order_page', views.order_page, name="order_page"),
]
    
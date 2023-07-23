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
    path('dashboard/products', views.products, name='products-page'),
    path('register', views.register, name='registrProcess'),
    path('loging', views.login, name="loginProcess"),
    #Kareem urls
    path('order_page', views.order_page, name="order_page"),
    path('order_list_process', views.order_list_process, name="order_list_process"),
    path('get_order_list', views.get_order_list, name="get_order_list"),
    path('remove_order_list/<int:order_id>', views.remove_order_list, name="remove_order_list"),
]
    
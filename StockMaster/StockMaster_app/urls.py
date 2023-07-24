from django.urls import path     
from StockMaster_app import views

app_name = 'SM_app'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/profile', views.profile, name='profile'),
    ########## Log and register #######################
    path('signup/', views.signup_page, name='signup-page'),
    path('login/', views.signin_page, name='signin-page'),
    path('register', views.register, name='registrProcess'),
    path('loging', views.login, name="loginProcess"),
    path('register', views.register, name='registrProcess'),
    path('loging', views.login, name="loginProcess"),
    ############### End LOG AND REG PROCESS ############
    ####### Prodcut Part ###############################
    path('display_products/<user_id>', views.display_products),
    path('save_products/', views.save_products, name='save_products'),
    # path('add_product', views.add_prodcut),
    ############# End product pathes ###################
]
    
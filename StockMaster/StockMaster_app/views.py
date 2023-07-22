from django.shortcuts import render, redirect, reverse
from .models import *
from .models import Prodcuts 
from django.contrib import messages
import date

# This function renders the homepage
def homepage(request):
    print ('hi')
    x = date.today()
    print(x)
    return render(request, 'homepage.html')

#This function renders the User Profile page upon button click
def profile(request):
    return render(request, 'users-profile.html')

#This function renders the dashboard after the user logs in to his acoount
def dashboard(request):
    context = {
       'username' :  request.session['user'],
       'user' : User.objects.get(id=request.session['user'])
    }
    return render(request, 'dashboard.html', context)

#This function renders the page that displays all products in the database
def products(request):
    return render(request, 'products-page.html')

################## Registration and Loging ################
#This function renders the sign up page upon button click
def signup_page(request):
    return render(request, 'pages-register2.html')

#This function for registration process
def register(request):
    errors = User.objects.regValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/signup')
    else:
        User.objects.create(
        f_name= request.POST['f_name'], 
        l_name= request.POST['l_name'], 
        s_name= request.POST['s_name'], 
        email=request.POST['email'], 
        password=request.POST['password'])
        return render(request, 'pages-login.html')

#This function renders the Log In page upon button click
def signin_page(request):
    return render(request, 'pages-login.html')

#This function for loging process
def login(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return render(request, 'pages-login.html')
    else:
        user = User.objects.get(email = request.POST['email'])
        request.session['user'] = user.id
        request.session['username'] = user.f_name
        return redirect('/dashboard')
    
#Page : Order Page
def order_page(request):
    return render(request,'orders_page.html')

#This function renders the "add new product" form
def add_prodcut(request):
    return render(request, 'add_product.html')

#This function handles POST data from "add new product" form and adds new PRODUCT to db:
def save_product(request):
    if request.method == 'POST':
        params = dict()
        
        params['p_name'] = request.POST.get('p_name')
        params['p_barcode'] = request.POST.get('p_barcode')
        params['expire_date'] = request.POST.get('expire_date')
        params['cost'] = request.POST.get('cost')
        params['sale_price'] = request.POST.get('sale_price')
        params['qty'] = request.POST.get('qty')
        
        Product.objects.create(**params)

    return redirect(reverse('products-page'))

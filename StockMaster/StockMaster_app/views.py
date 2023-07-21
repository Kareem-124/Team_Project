from django.shortcuts import render, redirect
from .models import * 
from django.contrib import messages


# This function renders the homepage
def homepage(request):
    return render(request, 'homepage.html')

#This function renders the User Profile page upon button click
def profile(request):
    return render(request, 'users-profile.html')

#This function renders the dashboard after the user logs in to his acoount
def dashboard(request):
    return render(request, 'dashboard.html')

#This function renders the page that displays all products in the database
def products(request):
    return render(request, 'products-page.html')

################## Registration and Loging ################
#This function renders the sign up page upon button click
def signup_page(request):
    return render(request, 'pages-register.html')

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
#THis function for loging process
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
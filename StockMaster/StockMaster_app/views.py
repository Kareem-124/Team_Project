from django.shortcuts import render, redirect, reverse
from .models import *
# from .models import Prodcuts 
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# This function renders the homepage
def homepage(request):
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
################# This is for Prodcut ####################################
#This function renders the page that displays all products in the database
def display_products(request, user_id):
    context = {
        'user' : User.objects.get(id=user_id)
    }
    return render(request, 'display_products-page.html', context)



def save_products(request):
    try:
        if request.method == 'POST':
            data = request.POST.get('data')
            try:
                products = json.loads(data)
                # Save products to the database
                for product in products:
                    new_product = Product(
                        p_name=product['p_name'],
                        p_barcode=int(product['p_barcode']),
                        expire_date=product['expire_date'],
                        cost=int(product['cost']),
                        qty=int(product['qty']),
                        user=User.objects.get(id=request.session.get('user'))
                    )
                    new_product.save()

                return JsonResponse({'message': 'Products saved successfully'})
            except Exception as e:
                return JsonResponse({'error': 'Error saving products: ' + str(e)}, status=500)
    except Exception as e:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
from django.shortcuts import render

# Create your views here.

# This function renders the homepage
def homepage(request):
    return render(request, 'homepage.html')

#This function renders the sign up page upon button click
def signup_page(request):
    return render(request, 'pages-register.html')

#This function renders the Log In page upon button click
def signin_page(request):
    return render(request, 'dashboard.html')

#This function renders the User Profile page upon button click
def profile(request):
    return render(request, 'users-profile.html')

#This function renders the dashboard after the user logs in to his acoount
def dashboard(request):
    return render(request, 'dashboard.html')

#This function renders the page that displays all products in the database
def products(request):
    return render(request, 'products-page.html')


def register(request):
    pass
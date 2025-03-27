from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.conf import settings
import os 
from .models import register_page,package,booking
from django.contrib import messages
import datetime
from django.db.models import Sum 
from django.core.mail import EmailMessage
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout 
from functools import wraps
# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']
        dob = request.POST['dob']
        gender = request.POST['gender']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        if register_page.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')

        user = register_page(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=make_password(password),  # Securely hashing the password
            dob=dob,
            gender=gender
        )
        user.save()
        messages.success(request, 'Registered successfully!')
        return redirect('login')  # Redirect to login page after registration

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = register_page.objects.get(email=email)  # Ensure correct model reference
            print(user.email)
            if check_password(password, user.password):  # Secure password check
                request.session['email'] = email
                request.session['firstName'] =user.first_name
                request.session['lastName'] = user.last_name
                print(email)
                request.session['is_logged_in'] = True  # Flag to check if user is logged in
                return redirect('index1')  # Redirect after login
            else:
                messages.error(request, 'Incorrect Password')
        except register_page.DoesNotExist:
            messages.error(request, 'Incorrect Email')

    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('index')

def index1(request):
    return render(request,'index1.html')

def gallery(request):
    return render(request,'gallery.html')

def packages(request):
    return render(request,'packages.html')

def kerala(request):
    place = package.objects.filter(place_name='kerala')
    return render(request,'kerala.html',{'place':place})

def goa(request):
    place = package.objects.filter(place_name='goa')
    return render(request,'goa.html',{'place':place})

def all_over(request):
    place = package.objects.filter(place_name='all_over')
    return render(request,'all_over.html',{'place':place})

def tamilnadu(request):
    place = package.objects.filter(place_name='tamilnadu')
    return render(request,'tamilnadu.html',{'place':place})

def manali(request):
    place = package.objects.filter(place_name='manali')
    return render(request,'manali.html',{'place':place})

def agra(request):
    place = package.objects.filter(place_name='agra')
    return render(request,'agra.html',{'place':place})

def booked(request,id):
    user_name = request.session.get('firstName')
    booking_details = get_object_or_404(package, id=id)
    return render(request,'bookings.html',{'booking_details':booking_details,'user_name':user_name})

def success_page(request,id):
    if request.method == 'POST':
        package_reference = get_object_or_404(package, id=id)
        journey_date = request.POST['journey_date']
        total_persons = request.POST['total_persons']
        pickup_location = request.POST['pickup_location']
        pickup_time = request.POST['pickup_time']
        first_name = request.session.get('firstName')
        last_name = request.session.get('lastName')
        email = request.session.get('email')
        save_booking = booking(
            book_now=package_reference,
            journey_date=journey_date,
            total_persons=total_persons,
            pickup_location=pickup_location,
            pickup_time=pickup_time,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        save_booking.save()
    bookings = booking.objects.all()
    return render(request,'success_page.html',{'bookings':bookings})

def dashboard(request):
    user = register_page.objects.all().count()
    booked = booking.objects.all().count()
    return render(request,'dashboard.html',{'user':user,'booked':booked})

def dashboard_packages(request):
    packages = package.objects.all()
    return render(request,'dashboard_package.html',{'packages':packages})

def dashboard_bookings(request):
    bookings = booking.objects.all()
    return render(request,'dashboard_booking.html',{'bookings':bookings})

def user_information(request):
    users = register_page.objects.all()
    return render(request,'user_information.html',{'users':users})

def logout2(request):
    request.session.flush()
    return redirect('index1')

from django.shortcuts import render,redirect
from . models import Car
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

# list of the whole fleet
def fleet(request):
    cars = Car.objects.all()

    context = {
        'page_title': "Our fleet",
        'cars': cars,
    }

    return render(
        request,
        'cars.html',
        context=context
    )


# details of selected car
def details(request, car_id):
    car = Car.objects.get(id=car_id)

    context = {
        'page_title': "Our fleet",
        'car': car,
    }

    return render(
        request,
        'details.html',
        context=context
    )

def log (request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('cars:rent_form')

    return render(request,
                  'cars/login.html')

def rent_form(request):

    return render(request,
                  'cars/rent_form.html')


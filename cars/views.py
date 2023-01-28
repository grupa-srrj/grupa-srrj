from django.shortcuts import render,redirect, get_object_or_404
from . models import Car, User, Order
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from django.contrib.auth.decorators import login_required


# list of the whole fleet
def fleet(request):
    cars = Car.objects.all()

    context = {
        'page_title': "Our fleet",
        'cars': cars,
    }

    return render(
        request,
        'cars/cars.html',
        context=context
    )


# details of selected car
def details(request, car_id):
    car = get_object_or_404(Car, id=car_id)


    context = {
        'page_title': "Our fleet",
        'car': car,
    }

    return render(
        request,
        'cars/details.html',
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
        else:
            messages.info(request,'Userame or password is incorrect')
            return render(request,
                          'cars/login.html')

    return render(request,
                  'cars/login.html')

#@login_required(login_url = 'login')
def rent_form(request):

    choice = Car.objects.all()

    if request.method == "POST":
        data = request.POST

        Order.objects.create(

            carr = ('choice')
        )


    return render(request,
                  'cars/rent_form.html',
                  context = {'choice':choice},
                )


def register(request):

    form=UserCreationForm()

    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Konto założone pomyslnie')

            return redirect('cars:login')

    return render(request,
                  'cars/register.html',
                  context={'form':form})

def logt(request):

    return redirect('cars:login')
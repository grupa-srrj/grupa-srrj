from django.shortcuts import render
from . models import Car
from django.shortcuts import get_object_or_404


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

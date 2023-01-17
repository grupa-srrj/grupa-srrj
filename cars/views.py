from django.shortcuts import render
from . models import Cars


# list of the whole fleet
def fleet(request):
    cars = Cars.objects.all()

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
    car = Cars.objects.get(id=car_id)

    context = {
        'page_title': "Our fleet",
        'car': car,
    }

    return render(
        request,
        'details.html',
        context=context
    )

# test for details
def test_details(request):

    context = {
        'page_title': "Our fleet",
    }

    return render(
        request,
        'details.html',
        context=context
    )

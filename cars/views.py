from django.shortcuts import render, get_object_or_404
from . models import Car, Order


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
                  context={'choice':choice},
                )

from django.shortcuts import render

def config(request):
    return render(
        request,
        'cars/cars.html'
    )


def adding(request):
    return render(
        request,
        'cars/adding.html'
    )


def subtraction(request):
    return render(
        request,
        'cars/subtraction.html'
    )


def edition(request):
    return render(
        request,
        'cars/edition.html'
    )


def our_fleet(request):
    return render(
        request,
        'cars/our_fleet.html'
    )


def details(request):
    return render(
        request,
        'cars/details.html'
    )
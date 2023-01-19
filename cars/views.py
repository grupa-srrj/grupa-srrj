from django.shortcuts import render
from cars.models import Cars
def list (request):

    list= Cars.objects.all()


    return render (request,
                   'cars/lista.html',
                   context= {'list':list}
                   )


def detail (request,id):

    car= Cars.objects.get(id=id)

    return render(request,
                  'cars/detail.html',
                  context={'car':car})
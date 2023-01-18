from django.shortcuts import render


def config(request):
    return render(
        request,
        'user/user.html'
    )

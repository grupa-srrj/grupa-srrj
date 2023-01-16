from django.shortcuts import render


def config(request):
    return render(
        request,
        'user/user.html'
    )


def login(request):
    return render(
        request,
        'user/login.html'
    )


def subtraction(request):
    return render(
        request,
        'user/subtraction.html'
    )


def signout(request):
    return render(
        request,
        'user/signout.html'
    )


def registration(request):
    return render(
        request,
        'user/registration.html'
    )


def password_recovery(request):
    return render(
        request,
        'user/password_recovery.html'
    )

from django.shortcuts import render


def homepage(request):

    context = {
        'page_title': "Car rental",
    }

    return render(
        request,
        'website/home.html',
        context=context
    )


def contact(request):

    context = {
        'page_title': "Contact us",
    }

    return render(
        request,
        'website/contact.html',
        context=context
    )



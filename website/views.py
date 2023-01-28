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


def privacy(request):

    context = {
        'page_title': "Privacy policy",
    }

    return render(
        request,
        'website/privacy.html',
        context=context
    )

def terms(request):

    context = {
        'page_title': "Terms and conditions",
    }

    return render(
        request,
        'website/terms.html',
        context=context
    )

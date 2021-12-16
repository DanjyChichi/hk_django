from django.shortcuts import render

from .models import MusinsaOuter


def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )


def show_musinsa(request):
    musinsa_items = MusinsaOuter.objects.all()
    return render(
        request,
        'single_pages/musinsa_items.html',
        {
            'items': musinsa_items
        }
    )
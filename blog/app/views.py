from django.shortcuts import render

# Create your views here.


def galeria(request):
    return render(
        request,
        'app/galeria.html',
        context={},
    )


def home(request):
    return render(
        request,
        'app/home.html',
        context={},
    )
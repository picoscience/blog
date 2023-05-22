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


def menu(request):
    return render(
        request,
        'app/menu.html',
        context={},
    )


def proyectos(request):
    return render(
        request,
        'app/proyectos.html',
        context={},
    )


def contacto(request):
    return render(
        request,
        'app/contacto.html',
        context={},
    )


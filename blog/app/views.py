from django.shortcuts import render

# Create your views here.


def galeria(request):
    return render(
        request,
        'app/galeria.html',
        context={},
    )
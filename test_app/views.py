from django.http import HttpResponse


def home_view(request):
    return HttpResponse('Hola, esta es una app de prueba para GCP...')

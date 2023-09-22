from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vistaUno (request):
    html="""
    <h1>App 1 funcionando correctamente</h1>
    """
    return HttpResponse(html)
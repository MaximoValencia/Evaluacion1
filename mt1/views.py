from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vistaUno (request):
    html="""
    <h1>App 1 funcionando correctamente</h1>
    <h2>Valoranchi</h2>
    <h3>completando etiqueta jaja</h3>
    <h4>Lo quiero profe^^</h4>
    """
    return HttpResponse(html)
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vistaUno (request):
    html="""
    <h1>Hola Mundo</h1>
    """
    return HttpResponse(html)
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vistaDos (request):
    html="""
    <h1>App 2 funcionando correctamente</h1>
    """
    return HttpResponse(html)
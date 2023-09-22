from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vistaDos (request):
    html="""
    <h1>App 2 funcionando correctamente</h1>
    <h2>Aguante colo colo</h2>
    <h3>LocoLoco</h3>
    <h4>Vio</h4>

    """
    return HttpResponse(html)
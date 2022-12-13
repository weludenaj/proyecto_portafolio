from cgitb import html

from django.shortcuts import render, HttpResponse


html_cabecera = """
<h1> Mi portafolio personal</h1>
<ul> 
    <li> <a href="/">Inicio </a> </li>
    <li> <a href="/about-me/">Acerca de </a> </li>
    <li> <a href="/">Contacto </a> </li>
</ul>
"""
# Create your views here.
def home(request):
    return render(request, 'core/home.html')




def portafolio(request):
    return render(request,'portfolio/portfolio.html')

def contacto(request):
    return render(request,'core/contacto.html')

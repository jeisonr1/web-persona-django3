from django.shortcuts import render, HttpResponse

html_base = """
<h1> Mi Web Personal</h1>
<ul>
    <li><a href="/">Portada</a></i>
    <li><a href="/about">Acerca de...</a></i>
    <li><a href="/portfolio">Portafolio</a></i>
    <li><a href="/contact">Contacto</a></i>    
</ul>
"""

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")



def contact(request):
    return render(request, "core/contact.html")
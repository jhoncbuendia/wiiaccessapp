from django.shortcuts import render
from directory.models import UsuarioApp
# Create your views here.

def index(request):
    aut = request.session.get('autenticado', False)
    if aut:
        if aut == 1:
    #if request.session['autenticado'] != 1:
            u = UsuarioApp.objects.filter(user = request.user)
            return render(request, 'usertools/index.html', { 'usuarioapp': u[0]})

    return render(request, 'usercontrol/index.html', {'mensaje': 'Ingrese sus datos'})
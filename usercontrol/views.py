from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from directory.models import UsuarioApp
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import logout
# Create your views here.

def index(request):

    return render(request, 'usercontrol/index.html')


def loginView(request):
    if request.method == 'POST':
        usuario = request.POST.get('user', 0)
        password = request.POST.get('password', 0)
        if usuario and password:
            user = authenticate(username=usuario, password=password)
            if user is not None:
                if user.is_active:

                    u = UsuarioApp.objects.filter(user = user)
                    if len(u):
                        print u
                        #return HttpResponse("ok")
                        login(request, user)
                        request.session['autenticado'] = 1
                        return redirect('/usertools')

                    request.session['autenticado'] = 0
                    return render(request, 'usercontrol/index.html', {'mensaje': 'Usuario Invalido'})
            else:
                request.session['error'] = 'Usuario Invalido'
                #return HttpResponse("Usuario invalido")
                return render(request, 'usercontrol/index.html', {'mensaje': 'Usuario Invalido'})
        else:
            request.session['error'] = 'Formulario Invalido'
            #return HttpResponse("formulario invalido")
            return render(request, 'usercontrol/index.html', {'mensaje': 'Formulario Invalido'})
    else:
        #return HttpResponse("Metodo de envio incorrecto")
        return render(request, 'usercontrol/index.html', {'mensaje': 'Metodo de envio incorrecto'})

def logout_view(request):
    logout(request)
    return render(request, 'usercontrol/index.html')

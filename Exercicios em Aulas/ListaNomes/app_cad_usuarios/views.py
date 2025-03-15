from django.shortcuts import render
from .models import Usuario


def home(request):
    return render(request, 'usuarios/home.html')


def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.name = request.POST.get('name')
    novo_usuario.age = request.POST.get('age')
    novo_usuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'usuarios/usuarios.html', usuarios)

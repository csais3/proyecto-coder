from django.shortcuts import render, redirect
from django.http import HttpResponse
from crud_rentakids.models import Cliente
from crud_rentakids.forms import ClienteForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/index.html', {'clientes': clientes})

def registrar_clientes(request):
    formulario = ClienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('/ver-clientes/')

    return render(request, 'clientes/crear.html', {'formulario': formulario})

def editar_clientes(request, id):
    cliente = Cliente.objects.get(id=id)
    formulario = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('/ver-clientes/')
    return render(request, 'clientes/editar.html', {'formulario': formulario})

def eliminar(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('/ver-clientes/')
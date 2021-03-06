"""project_rentakids URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from crud_rentakids.views import inicio, nosotros, ver_clientes, registrar_clientes, editar_clientes, eliminar

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('nosotros/', nosotros, name = 'nosotros'),
    path('ver-clientes/', ver_clientes, name = 'ver-clientes'),
    path('ver-clientes/registrar', registrar_clientes, name = 'registrar-clientes'),
    path('ver-clientes/editar', editar_clientes, name = 'editar-clientes'),
    path('eliminar/<int:id>', eliminar, name='eliminar'),
    path('ver-clientes/editar/<int:id>', editar_clientes, name = 'editar-clientes'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

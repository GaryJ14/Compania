from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    #MODELO Empresa
    path('ListadoEmpresa/',views.ListadoEmpresa,name="ListadoEmpresa"),
    path('nuevaEmpresa/',views.nuevaEmpresa, name='nuevaEmpresa'),
    path('guardarEmpresa/',views.guardarEmpresa, name='guardarEmpresa'),
    path('eliminarEmpresa/<id>',views.eliminarEmpresa, name='eliminarEmpresa'),
    path('editarEmpresa/<id>',views.editarEmpresa, name='editarEmpresa'),
    path('procesarActualizacionEmpresa',views.procesarActualizacionEmpresa, name='procesarActualizacionEmpresa'),
  #MODELO EMPLEADO
    path('ListadoEmpleado/',views.ListadoEmpleado,name="ListadoEmpleado"),
    path('nuevoEmpleado/',views.nuevoEmpleado, name='nuevoEmpleado'),
    path('guardarEmpleado/',views.guardarEmpleado, name='guardarEmpleado'),
    path('eliminarEmpleado/<id>',views.eliminarEmpleado, name='eliminarEmpleado'),
    path('editarEmpleado/<id>',views.editarEmpleado, name='editarEmpleado'),
    path('procesarActualizacionEmpleado',views.procesarActualizacionEmpleado, name='procesarActualizacionEmpleado'),
    
    path('enviar_correo/',views.enviar_correo, name='enviar_correo'),

]
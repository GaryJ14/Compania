
from django.shortcuts import render, redirect
from .models import Empresas, Empleados
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
   
    
    return render (request,"home.html")


#Funcion listado raza
def ListadoEmpresa(request):
    empresabdd=Empresas.objects.all()
    return render(request,"ListadoEmpresa.html",{'empresa':empresabdd})

#Renderizando el formulario 
def nuevaEmpresa(request):
   return render(request,'nuevaEmpresa.html')

#Insertando datos en la base de datos
def guardarEmpresa(request):
    nombre_empr=request.POST["nombre_empr"]
    direccion_empr=request.POST["direccion_empr"]
    telefono_empr=request.POST["telefono_empr"]
    email_empr=request.POST["email_empr"]
    fundacion_empr=request.POST["fundacion_empr"]
    sector_empr=request.POST["sector_empr"]

    nuevaEmpresa=Empresas.objects.create(nombre_empr=nombre_empr, direccion_empr=direccion_empr, telefono_empr=telefono_empr,email_empr=email_empr, fundacion_empr=fundacion_empr, sector_empr=sector_empr)
    messages.success(request,"Empresa guardada exitosamente.")
    return redirect('ListadoEmpresa')

#Se recibe el id para eliminar una raza
def eliminarEmpresa(request,id):
    empresaEliminar=Empresas.objects.get(id_empr=id)
    empresaEliminar.delete()
    messages.success(request,"Empresa eliminada exitosamente.")
    return redirect('ListadoEmpresa')

# Renderizando formulario de actualizacion
def editarEmpresa(request,id):
    empresaEditar=Empresas.objects.get(id_empr=id)
    return render(request,'editarempresa.html',{'editarempresa':empresaEditar})

#Actualizando los datos en la base de datos
def procesarActualizacionEmpresa(request):
    id_empr=request.POST["id_empr"]
    nombre_empr=request.POST["nombre_empr"]
    direccion_empr=request.POST["direccion_empr"]
    telefono_empr=request.POST["telefono_empr"]
    email_empr=request.POST["email_empr"]
    fundacion_empr=request.POST["fundacion_empr"]
    sector_empr=request.POST["sector_empr"]
    empresaConsultado=Empresas.objects.get(id_empr=id_empr)
    empresaConsultado.nombre_empr=nombre_empr
    empresaConsultado.direccion_empr=direccion_empr
    empresaConsultado.telefono_empr=telefono_empr
    empresaConsultado.email_empr=email_empr
    empresaConsultado.fundacion_empr=fundacion_empr
    empresaConsultado.sector_empr=sector_empr

    empresaConsultado.save()
    messages.success(request,"Empresa actualizado exitosamente.")
    return redirect('ListadoEmpresa')

#----------------------------EMPLEADOS------------------------------------
def ListadoEmpleado(request):
    empladobdd=Empleados.objects.all()
    return render(request,"ListadoEmpleado.html",{'empleado':empladobdd})


# Renderizando el formulario
def nuevoEmpleado(request):
    empresas = Empresas.objects.all()
    return render(request, 'nuevoEmpleado.html', {'empresas': empresas})

# Insertando datos en la base de datos

#Insertando datos en la base de datos
def guardarEmpleado(request):
    if request.method == 'POST':
        nombre_empl=request.POST["nombre_empl"]
        apellido_empl=request.POST["apellido_empl"]
        salario_empl=request.POST["salario_empl"]
        puesto_empl=request.POST["puesto_empl"]
        email = request.POST["email"]
        id=request.POST["empresa"]
        foto_empl=request.FILES.get("foto_empl")

        id_empr = Empresas.objects.get(id_empr=id)

        nuevoEmpleado=Empleados.objects.create(
            nombre_empl=nombre_empl, 
            apellido_empl=apellido_empl, 
            salario_empl=salario_empl,
            puesto_empl=puesto_empl,
            email=email, 
            id_empr=id_empr, 
            foto_empl=foto_empl)
        messages.success(request,"Empleado guardada exitosamente.")
        email1="joelcalero2002@gmail.com"
        # Construir y enviar el correo electrónico
        subject = 'Nuevo Empleado guardado'
        message = (
            f'Se ha guardado exitosamente el empleado "{nombre_empl}".\n\n'
            f'Detalles:\n'
            f'Nombre: {nombre_empl}\n'
            f'Dirección: {apellido_empl}\n'
            f'Salario: {salario_empl}\n'
            f'Puesto: {puesto_empl}\n'
            f'Email: {email}\n'
            
            
        )
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,  # Sender email address
            [email1],
            fail_silently=False,
        )
        return redirect('ListadoEmpleado')
    return render(request, 'ListadoEmpleado.html')
    
def eliminarEmpleado(request,id):
    empleadoEliminar=Empleados.objects.get(id_empl=id)
    empleadoEliminar.delete()
    messages.success(request,"Empleado eliminada exitosamente.")
    return redirect('ListadoEmpleado')

# Renderizando formulario de actualizacion
def editarEmpleado(request,id):
    editarEmpleado=Empleados.objects.get(id_empl=id)
    empresas = Empresas.objects.all()
    return render(request,'editarEmpleado.html',{'editarEmpleado':editarEmpleado, 'empresas':empresas })

#Actualizando los datos en la base de datos
def procesarActualizacionEmpleado(request):
    id_empl=request.POST["id_empl"]
    nombre_empl=request.POST["nombre_empl"]
    apellido_empl=request.POST["apellido_empl"]
    salario_empl=request.POST["salario_empl"]
    puesto_empl=request.POST["puesto_empl"]
    id_empr=request.POST["empresa"]
    foto_empl=request.FILES.get["foto_empl"]

    empleadoConsultado=Empleados.objects.get(id_empl=id_empl)
    empresaConsultado=Empresas.objects.get(id_empr=id_empr)

    empleadoConsultado.nombre_empl=nombre_empl
    empleadoConsultado.apellido_empl=apellido_empl
    empleadoConsultado.salario_empl=salario_empl
    empleadoConsultado.puesto_empl=puesto_empl
    empleadoConsultado.id_empr=empresaConsultado
    empleadoConsultado.foto_empl=foto_empl

    empleadoConsultado.save()
    messages.success(request,"Empleado actualizado exitosamente.")
    return redirect('ListadoEmpleado')


#PARA MANDAR UN CORREO

def enviar_correo(request):
    if request.method == 'POST':
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        message=request.POST["message"]
        email1="joelcalero2002@gmail.com"

        # Construir y enviar el correo electrónico
        subject = 'Nuevo mensaje guardado'
        message = (
            f'Se ha guardado exitosamente el mensaje de:  "{name}".\n\n'
            f'Detalles:\n'
            f'email: {email}\n'
            f'phone: {phone}\n'
            f'message: {message}\n'
            
        )
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,  # Sender email address
            [email1],
            fail_silently=False,
        )
        return render (request,"home.html")
    
    return render (request,"home.html")
   



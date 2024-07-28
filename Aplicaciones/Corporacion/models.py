from django.db import models

class Empresas(models.Model):
    id_empr=models.AutoField(primary_key=True)
    nombre_empr=models.CharField(max_length=100)
    direccion_empr=models.CharField(max_length=100)
    telefono_empr=models.CharField(max_length=50)
    email_empr=models.CharField(max_length=150,default='')
    fundacion_empr=models.DateField()
    sector_empr=models.CharField(max_length=150,default='')

    def __str__(self):
        fila="{0}: {1} - {2} - {3} - {4} -{5} - {6}"
        return fila.format(self.id_empr,self.nombre_empr,self.direccion_empr,self.telefono_empr,self.email_empr,self.fundacion_empr,self.sector_empr)
    
class Empleados(models.Model):
    id_empl = models.AutoField(primary_key=True)
    nombre_empl=models.CharField(max_length=25)
    apellido_empl=models.CharField(max_length=150,default='')
    salario_empl=models.IntegerField()
    puesto_empl=models.CharField(max_length=150,default='')
    id_empr = models.ForeignKey(Empresas,on_delete=models.CASCADE)
    foto_empl=models.FileField(upload_to='empleados',null=True,blank=True)
    email=models.EmailField(null=True, blank=True)

#Para la estructura que aparezca en la base de datose
    def __str__(self):
        fila="{0}: {1} - {2} - {3} - {4} -{5} - {6}"
        return fila.format(self.id_empl,self.nombre_empl,self.apellido_empl,self.salario_empl,self.puesto_empl,self.id_empr,self.foto_empl)


from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Empresa(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    def __unicode__(self):
        return self.nombre

class Taladro(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    telefono_ppal = models.CharField(max_length=100, null=True)
    correo_ppal = models.CharField(max_length=100, null=True)
    correo_sec = models.CharField(max_length=100, null=True)
    empresa = models.ForeignKey(Empresa, null=True)
    favorito = models.ForeignKey('Favorito', null = True, blank = True)
    def __unicode__(self):
        return self.nombre

class Extension(models.Model):
    nro_extension = models.CharField(max_length=100,null=True)
    responsable = models.CharField(max_length=100,null=True)
    taladro = models.ForeignKey(Taladro,null=True)
    def __unicode__(self):
        return self.nro_extension

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100, null=True)
    correo_contacto = models.CharField(max_length=100, null=True)
    empresa = models.ForeignKey(Empresa, null=True)
    favorito = models.ForeignKey('Favorito', null = True, blank = True)

    def __unicode__(self):
        return self.nombre

class UsuarioApp(models.Model):
    user = models.OneToOneField(User, null=True, related_name = 'user_app')
    correo_contacto = models.CharField(max_length=100, null=True)
    empresa = models.ForeignKey(Empresa,null=True)
    def __unicode__(self):
        return self.user.username

class AlertaPanico(models.Model):
    email = models.CharField(max_length=100, null=True)
    usuario = models.ForeignKey(UsuarioApp, null=True)
    def __unicode__(self):
        return self.email

class ProveedorGlobal(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100, null=True)
    correo_contacto = models.CharField(max_length=100, null=True)
    def __unicode__(self):
        return self.nombre

class Favorito(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    telefono = models.CharField(max_length=100, null=True)
    correo = models.CharField(max_length=100, null=True)
    usuario = models.ForeignKey(UsuarioApp,null=True)
    tipo = models.CharField(max_length=100,null=True)
    direccion = models.CharField(max_length=100, null=True)
    def __unicode__(self):
        return self.telefono


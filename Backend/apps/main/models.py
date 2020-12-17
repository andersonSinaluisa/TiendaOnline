from django.db import models
from apps.mant.models import *

class ConfRol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    acciones = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        db_table = 'conf_rol'

    def __str__(self):
        return self.codigo, self.nombre, self.descripcion


class ConfTienda(models.Model):
    id_tienda = models.AutoField(primary_key=True)
    ruc = models.CharField(max_length=13, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    etiquetas = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Tienda'
        verbose_name_plural = 'Tiendas'
        db_table = 'conf_tienda'

    def __str__(self):
        return self.nombre, self.ruc





class ConfUsuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50, blank=True, null=True)
    contrasenia = models.CharField(max_length=50, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    id_rol = models.ForeignKey(ConfRol, on_delete=models.CASCADE, related_name='fk_admin_rol', db_column='id_rol')
    id_persona = models.ForeignKey(MantPersona, on_delete=models.CASCADE, related_name='fk_admin_persona', db_column='id_persona')

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'
        db_table = 'conf_admin'

    def __str__(self):
        return self.usuario


class ConfUsuarioTienda(models.Model):
    id_usuario_tienda = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50, blank=True, null=True)
    contrasenia = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    id_rol = models.ForeignKey(ConfRol, on_delete=models.CASCADE, related_name='fk_usuario_tienda_rol', db_column='id_rol')
    id_persona = models.ForeignKey(MantPersona, on_delete=models.CASCADE, related_name='fk_usuario_tienda_persona', db_column='id_persona')
    id_tienda = models.ForeignKey(ConfTienda, on_delete=models.CASCADE, related_name='fk_usuario_tienda_tienda', db_column='id_tienda')

    class Meta:
        verbose_name = 'Usuario Tienda'
        verbose_name_plural = 'Usuario Tienda'
        db_table = 'conf_usuario_tienda'

    def __str__(self):
        return self.usuario, self.email


#------------------------------------------------------módulo de movimientos

from django.db import models
from apps.mant.models import *
# Create your models here.

class MovSesion(models.Model):
    id_sesion = models.AutoField(primary_key=True)
    token = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    id_usuario = models.ForeignKey('main.ConfUsuario', on_delete=models.CASCADE, related_name='fk_sesion_usuario', db_column='id_usuario')

    class Meta:
        verbose_name = 'Sesion'
        verbose_name_plural = 'Sesiones'
        db_table = 'mov_sesion'

    def __str__(self):
        return self.token, self.tipo


class MovIngreso(models.Model):
    id_ingreso = models.AutoField(primary_key=True)
    tipo_comprobante = models.CharField(max_length=50, blank=True, null=True)
    serie_comprobante = models.CharField(max_length=10, blank=True, null=True)
    num_comprobante = models.CharField(max_length=10, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    iva = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    
    id_proveedor = models.ForeignKey(MantProveedor, on_delete=models.CASCADE, related_name='fk_ingreso_proveedor', db_column='id_proveedor')
    id_usuario = models.ForeignKey('main.ConfUsuario', on_delete=models.CASCADE, related_name='fk_ingreso_usuario', db_column='id_usuario')
    id_tienda = models.ForeignKey('main.ConfTienda', on_delete=models.CASCADE, related_name='fk_ingreso_tienda', db_column='id_tienda')

    class Meta:
        verbose_name = 'Ingreso'
        verbose_name_plural = 'Ingresos'
        db_table = 'mov_ingreso'
    
    def __str__(self):
        return self.tipo_comprobante, self.serie_comprobante, self.num_comprobante


class MovDetalleIngreso(models.Model):
    id_detalle_ingreso = models.AutoField(primary_key=True)
    id_ingreso = models.ForeignKey(MovIngreso, on_delete=models.CASCADE, related_name='fk_detalle_ingreso_ingreso', db_column='id_ingreso')
    id_producto = models.ForeignKey(MantProducto, on_delete=models.CASCADE, related_name='fk_detalle_ingreso_producto', db_column='id_producto')
    cantidad = models.IntegerField(blank=True, null=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    id_tienda = models.ForeignKey('main.ConfTienda', on_delete=models.CASCADE, related_name='fk_detalle_ingreso_tienda', db_column='id_tienda')

    class Meta:
        verbose_name = 'DetalleIngreso'
        verbose_name_plural = 'DetalleIngresos'
        db_table = 'mov_detalle_ingreso'


class MovNotificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    id_usuario = models.ForeignKey('main.ConfUsuario', on_delete=models.CASCADE, related_name='fk_notificacion_usuario', db_column='id_usuario')

    class Meta:
        verbose_name = 'Notificacion'
        verbose_name_plural = 'Notificaciones'
        db_table = 'mov_notificacion'

    def __str__(self):
        return self.descripcion

    
class MovVenta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    tipo_comprobante = models.CharField(max_length=50, blank=True, null=True)
    serie_comprobante = models.CharField(max_length=10, blank=True, null=True)
    num_comprobante = models.CharField(max_length=10, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    iva = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    
    id_usuario = models.ForeignKey('main.ConfUsuario', on_delete=models.CASCADE, related_name='fk_venta_usuario', db_column='id_usuario')
    id_tienda = models.ForeignKey('main.ConfTienda', on_delete=models.CASCADE, related_name='fk_venta_tienda', db_column='id_tienda')

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'mov_venta'

    def __str__(self):
        return self.tipo_comprobante, self.serie_comprobante, self.num_comprobante


class MovDetalleVenta(models.Model):
    id_detalle_venta = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(MovVenta, on_delete=models.CASCADE, related_name='fk_detalle_venta_venta', db_column='id_venta')
    id_producto = models.ForeignKey(MantProducto, on_delete=models.CASCADE, related_name='fk_detalle_venta_producto', db_column='id_producto')
    cantidad = models.IntegerField(blank=True, null=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    id_tienda = models.ForeignKey('main.ConfTienda', on_delete=models.CASCADE, related_name='fk_detalle_venta_tienda', db_column='id_tienda')

    class Meta:
        verbose_name = 'DetalleVenta'
        verbose_name_plural = 'DetalleVentas'
        db_table = 'mov_detalle_venta'

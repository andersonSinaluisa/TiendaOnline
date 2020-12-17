from django.db import models

# Create your models here.

class MantCategoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    id_tienda = models.ForeignKey('main.ConfTienda', on_delete=models.CASCADE, related_name='fk_categoria_tienda', db_column='id_tienda')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'mant_categoria'

    def __str__(self):
        return self.nombre
    

class MantPersona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=30, blank=True, null=True)
    apellidos = models.CharField(max_length=30, blank=True, null=True)
    identificacion = models.CharField(max_length=10, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    genero = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True)
    foto = models.FileField(null=True)
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table = 'mant_persona'

    def __str__(self):
        return self.nombres, self.apellidos


class MantProducto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    imagen_url = models.TextField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    talla = models.TextField(blank=True, null=True)

    id_categoria = models.ForeignKey(MantCategoria, on_delete=models.CASCADE, related_name='fk_producto_categoria', db_column='id_categoria')
    id_tienda = models.ForeignKey('main.ConfTienda', on_delete=models.CASCADE, related_name='fk_producto_tienda', db_column='id_tienda')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'mant_producto'

    def __str__(self):
        return self.codigo, self.nombre


class MantRedSocial(models.Model):
    id_red = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    id_tienda = models.ForeignKey('main.ConfTienda', on_delete=models.CASCADE, related_name='fk_red_tienda', db_column='id_tienda')

    class Meta:
        verbose_name = 'RedSocial'
        verbose_name_plural = 'RedesSociales'
        db_table = 'mant_redsocial'

    def __str__(self):
        return self.nombre, self.link


class MantProveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    identificacion = models.CharField(max_length=13, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'mant_proveedor'

    def __str__(self):
        return self.nombre, self.identificacion, self.descripcion
from django.db import models

#---------------------------------------------------------------módulo de mantenimiento

class MantCategoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    id_tienda = models.ForeignKey(ConfTienda, on_delete=models.CASCADE, related_name='fk_categoria_tienda', db_column='id_tienda')

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
    id_tienda = models.ForeignKey(ConfTienda, on_delete=models.CASCADE, related_name='fk_producto_tienda', db_column='id_tienda')

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
    id_tienda = models.ForeignKey(ConfTienda, on_delete=models.CASCADE, related_name='fk_red_tienda', db_column='id_tienda')

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

#---------------------------------------------------------módulo de configuración

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
    uid = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    photo_url = models.TextField(blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    id_rol = models.ForeignKey(ConfRol, on_delete=models.CASCADE, related_name='fk_usuario_rol', db_column='id_rol')
    id_persona = models.ForeignKey(MantPersona, on_delete=models.CASCADE, related_name='fk_usuario_persona', db_column='id_persona')
    id_tienda = models.ForeignKey(ConfTienda, on_delete=models.CASCADE, related_name='fk_usuario_tienda', db_column='id_tienda')

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'conf_usuario'

    def __str__(self):
        return self.uid, self.nombre


class ConfAdmin(models.Model):
    id_rol = models.AutoField(primary_key=True)
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

class MovSesion(models.Model):
    id_sesion = models.AutoField(primary_key=True)
    token = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    id_usuario = models.ForeignKey(ConfUsuario, on_delete=models.CASCADE, related_name='fk_sesion_usuario', db_column='id_usuario')

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
    id_usuario = models.ForeignKey(ConfUsuario, on_delete=models.CASCADE, related_name='fk_ingreso_usuario', db_column='id_usuario')
    id_tienda = models.ForeignKey(ConfTienda, on_delete=models.CASCADE, related_name='fk_ingreso_tienda', db_column='id_tienda')

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
    id_tienda = models.ForeignKey(ConfTienda, on_delete=models.CASCADE, related_name='fk_detalle_ingreso_tienda', db_column='id_tienda')

    class Meta:
        verbose_name = 'DetalleIngreso'
        verbose_name_plural = 'DetalleIngresos'
        db_table = 'mov_detalle_ingreso'


class MovNotificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    id_usuario = models.ForeignKey(ConfUsuario, on_delete=models.CASCADE, related_name='fk_notificacion_usuario', db_column='id_usuario')

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
    
    id_usuario = models.ForeignKey(ConfUsuario, on_delete=models.CASCADE, related_name='fk_venta_usuario', db_column='id_usuario')
    id_tienda = models.ForeignKey(ConfTienda, on_delete=models.CASCADE, related_name='fk_venta_tienda', db_column='id_tienda')

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
    id_tienda = models.ForeignKey(ConfTienda, on_delete=models.CASCADE, related_name='fk_detalle_venta_tienda', db_column='id_tienda')

    class Meta:
        verbose_name = 'DetalleVenta'
        verbose_name_plural = 'DetalleVentas'
        db_table = 'mov_detalle_venta'

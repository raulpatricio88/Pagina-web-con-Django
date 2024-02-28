from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria = models.CharField(max_length=50, blank=True, verbose_name='Nombre de Categoria')

    def __str__(self):
        return self.nombreCategoria  


class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id Producto')
    nombreProducto = models.CharField(max_length=50, blank=True, verbose_name='Nombre Producto') 
    descripcionProducto = models.CharField(max_length=100, blank=True, verbose_name='Descripcion Producto')
    imagen=models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name='Imagen')
    categoriaProducto = models.ForeignKey(Categoria, default=1, on_delete=models.CASCADE, verbose_name='Categoria')
    precioProducto = models.IntegerField(verbose_name='Precio Producto')
    stockProducto = models.IntegerField(verbose_name='Stock Producto')

    def __str__(self):
        return self.nombreProducto
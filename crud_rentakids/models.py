from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, verbose_name='Nombre del Cliente')
    telefono = models.CharField(max_length=255, verbose_name='Teléfono')
    email = models.EmailField(max_length=254, verbose_name='Email')
    imagen = models.ImageField(upload_to='images/', verbose_name='Imagen', null=True)
    notas = models.TextField(verbose_name='Notas', null=True)

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + " Teléfono: " + self.telefono + " - " + " Email: " + self.email + " - " + " Notas: " + self.notas
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

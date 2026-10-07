from django.db import models

class Libro(models.Model):

    isbn = models.CharField(
        max_length= 17,
        unique= True
    )

    titulo = models.CharField(
        max_length= 100
    )

    autor = models.CharField(
        max_length= 100
    )

    anio_publicacion = models.PositiveIntegerField()

    cant_total = models.PositiveIntegerField(
        default= 0
    )

    cant_disponible = models.PositiveIntegerField(
        default= 0
    )



class Socio(models.Model):

    nombre = models.CharField(
        max_length= 20
    )

    apellido = models.CharField(
        max_length= 30
    )

    dni = models.PositiveIntegerField()

    mail = models.EmailField(
        max_length= 200,
        unique= True
    )

    estado = models.BooleanField(
        default= True
    )


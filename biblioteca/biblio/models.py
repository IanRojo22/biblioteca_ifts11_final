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

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.anio_publicacion})"


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

    def __str__(self):
        return f"N {self.id} - {self.apellido} {self.nombre}"


class Reserva(models.Model):

    class Estados_de_reserva(models.TextChoices):
        PENDIENTE = "PENDIENTE", "Pendiente"
        RETIRADA = "RETIRADA", "Retirada"
        CANCELADA = "CANCELADA", "Cancelada"
        FINALIZADA = "FINALIZADA", "Finalizada"

    socio = models.ForeignKey(
        Socio, 
        on_delete=models.PROTECT,
        related_name="reservas"
    )

    libro = models.ForeignKey(
        Libro,
        on_delete=models.PROTECT,
        related_name="reservas"
    )

    estado_reserva = models.CharField(
        max_length= 10,
        choices= Estados_de_reserva.choices,
        default=  Estados_de_reserva.PENDIENTE
    )

    def __str__(self):
        return f"Reserva {self.estado_reserva} - {self.libro.titulo} - {self.socio.nombre} {self.socio.apellido}"

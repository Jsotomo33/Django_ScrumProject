from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group

# Create your models here.

class Projecte(models.Model):
	nom = models.CharField(max_length=200, help_text="Nombre del proyecto")
	descripcion = models.TextField(blank=True, null=True, default="Un nuevo proyecto..")
	scrum_master = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="scrum_master")
	product_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="product_owner")

	grup = models.ForeignKey(Group, on_delete=models.CASCADE,)

	def __str__(self):
		return self.nom

class Sprint(models.Model):
	projecte = models.ForeignKey(Projecte, on_delete=models.CASCADE)
	data_inici = models.DateField()
	data_final = models.DateField()
	hores = models.IntegerField(default = 0, help_text="Horas de desarrollo disponibles de los miembros del equipo")




class Spec(models.Model):
	DIFICULTAT = (
		("D", "Desconeguda"),
		("B", "Baixa"),
		("M", "Mitjana"),
		("A", "Alta"),
		)
	descripcion = models.TextField()
	dificultat = models.CharField(max_length=1, choices = DIFICULTAT, default = "D")
	hores = models.IntegerField(default = 0)

	developer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
	sprint = models.ForeignKey(Sprint, on_delete= models.CASCADE,null=True, blank=True)
	projecte = models.ForeignKey(Projecte, on_delete= models.CASCADE,)

	def __str__(self):
		return self.descripcion



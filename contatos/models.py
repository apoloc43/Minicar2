from django.db import models

# Create your models here.


class Amigo(models.Model):
    info = models.CharField("Marca", max_length=100,)
    modelo = models.CharField("Modelo" ,max_length=100,default="")
    ano_fabricacao = models.IntegerField(default=2023)
    

    imagens = models.ImageField("Imagens", upload_to="imagens", blank=True, null=True)

    def __str__(self):
        return self.modelo

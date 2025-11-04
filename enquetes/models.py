from django.db import models

class Enquete(models.Model):
    pergunta = models.CharField(max_length=200)
    data_pub = models.DateTimeField("data de publicação")

    def __str__(self):
        return self.pergunta


class Choice(models.Model):
    enquete = models.ForeignKey(Enquete, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.texto

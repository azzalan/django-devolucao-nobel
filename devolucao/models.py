from django.db import models

class Livro(models.Model):
    isbn = models.CharField(max_length=15)
    titulo = models.CharField(max_length=150)
    quantidade_total_a_devolver = models.IntegerField()
    quantidade_faltando = models.IntegerField()

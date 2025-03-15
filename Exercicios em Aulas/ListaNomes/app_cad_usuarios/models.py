from django.db import models


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)
    age = models.IntegerField()

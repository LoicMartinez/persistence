from django.db import models

from app.components.marque.model import Marque


class Voiture(models.Model):

    name = models.TextField()
    color = models.TextField()
    marque = models.ForeignKey(Marque, on_delete=models.CASCADE, null=True, related_name='voitures')

    def __str__(self):
        return self.name


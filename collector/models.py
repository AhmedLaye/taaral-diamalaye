from django.db import models

# Create your models here.
class Poete(models.Model):
    nom = models.CharField(max_length=100)
    lieu_de_naissance = models.CharField(max_length=100)
    date_de_naissance = models.DateField()

    def __str__(self):
        return self.nom

class Poeme(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.ForeignKey(Poete, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_de_creation = models.DateField(auto_now_add=True)
    didie_a = models.CharField(max_length=200)
    ecrit_le = models.DateField()

    def __str__(self):
        return self.titre
from django.db import models
from django.contrib.auth.models import User

class Kategorie(models.Model):
    nazev = models.CharField(max_length=100)

    def __str__(self):
        return self.nazev

class Recept(models.Model):
    nazev = models.CharField(max_length=200)
    popis = models.TextField()
    postup = models.TextField()
    doba_pripravy = models.IntegerField(help_text="Čas v minutách")
    pocet_porci = models.IntegerField()
    kategorie = models.ForeignKey(Kategorie, on_delete=models.SET_NULL, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fotka = models.ImageField(upload_to='recepty/', blank=True, null=True)
    datum_pridani = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nazev

class Hodnoceni(models.Model):
    recept = models.ForeignKey(Recept, on_delete=models.CASCADE, related_name='hodnoceni')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    hvezdicky = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    komentar = models.TextField(blank=True)

    def __str__(self):
        return f"{self.recept} - {self.hvezdicky}⭐"
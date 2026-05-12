from django import forms
from .models import Recept

class ReceptForm(forms.ModelForm):
    class Meta:
        model = Recept
        fields = ['nazev', 'popis', 'postup', 'doba_pripravy', 'pocet_porci', 'kategorie', 'fotka']
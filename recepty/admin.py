from django.contrib import admin
from .models import Kategorie, Recept, Hodnoceni

admin.site.register(Kategorie)
admin.site.register(Recept)
admin.site.register(Hodnoceni)
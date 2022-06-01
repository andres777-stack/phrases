from django.contrib import admin
from .models import Phrase

@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin): #Para entender cómo se da esto hay que ver el __init__.py del folders admin. 
    model = Phrase
    list_display = ['sentence', 'author', 'created', 'updated'] #Propiedad, que tiene por defecto una tupla con __str__. 
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('slug', 'created', 'updated')
        return ()


# Register your models here.

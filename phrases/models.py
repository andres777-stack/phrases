from django.db import models
from django.urls import reverse

class Phrase(models.Model):
    author = models.CharField(max_length=50)
    sentence = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('phrases:detail', args=[str(self.pk)]) #se recordará que se podía usar rutas nombradas. 
    #_ahora vemos que se puede también poner argumentos de forma característica. ¿Por qué un str si espera un int?

    def __str__(self):
        if len(self.sentence) > 15:
            return f'{self.sentence[:15]}...({self.author})'
        else:
            return f'{self.sentence} ({self.author})'
# Create your models here.

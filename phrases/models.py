from django.db import models
from django.urls import reverse
from common.utils.text import unique_slug

class Phrase(models.Model):
    author = models.CharField(max_length=50)
    sentence = models.TextField(max_length=255)
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self) #método __str__()
            self.slug = unique_slug(value, type(self)) #Belleza de código. 
        super().save(*args, **kwargs) # invocar super().save() para hacer lo que el método save() hace para guardar.

    def get_absolute_url(self):
        #return reverse('phrases:detail', args=[str(self.pk)]) #se recordará que se podía usar rutas nombradas. 
    #_ahora vemos que se puede también poner argumentos de forma característica. ¿Por qué un str si espera un int?
        return reverse('phrases:detail', args=[self.slug]) #se utiliza slug en vez de la PK. 
    def __str__(self):
        if len(self.sentence) > 15:
            return f'{self.sentence[:15]}...({self.author})'
        else:
            return f'{self.sentence} ({self.author})'
# Create your models here.

from django import template
import random

from phrases.models import Phrase

register = template.Library()

@register.inclusion_tag('common/phrase.html')
def random_phrase():
    count = Phrase.objects.count()
    if count > 0:
        i = random.randint(0, count-1)
        phrase = Phrase.objects.all()[i]
        return {'phrase': phrase}
    else:
        return {'phrase': {'sentence': 'NO hay phrases en la base de datos', 'author': 'Admin'}}
        #Debe ir como dict pues va como contexto al template señalado más arriba como argumento.
        # Será un template anidado en otro mediante este tag personalizado.  

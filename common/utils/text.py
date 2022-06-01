import random
import string

from django.utils.text import slugify #text es un archivo.py, y slugify es una función. 

def unique_slug(s, model, num_chars=50):
    '''
    Return slug of num_chars length unique to model
    's' is the string to turn into a slug
    'model' is the model we need to use to check for uniqueness
    '''
    slug = slugify(s)
    #convierte espacios a guiones. Elimina lo que no es sean caracteres alfanumericos, guiones o guiones bajos. 
    slug = slug[:num_chars].strip('-') #Devuelve la misma cadena con los espacios iniciales y finales eliminados
    #_se puede pasar un parámetro para señalar qué eliminar. 
    while True:
        dup = model.objects.filter(slug=slug)
        if not dup: #si no está en la base de datos, por lo tanto, el slug es único y se retorna. 
            return slug
        else: #no es único, por lo tanto hay que hacerlo único random:
            slug = slug[:39] + '-' + random_string(10)
            
        

def random_string(num_chars=3):
    letters = string.ascii_lowercase #de la a hasta la z.
    rs = ''.join(random.choice(letters) for i in range(num_chars)) #se señala las veces que tiene que iterar. 
    return rs


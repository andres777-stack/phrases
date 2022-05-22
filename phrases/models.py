from django.db import models

class Phrase(models.Model):
    author = models.CharField(max_length=50)
    sentence = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.sentence) > 15:
            return f'{self.sentence[:15]}...({self.author})'
        else:
            return f'{self.sentence} ({self.author})'
# Create your models here.

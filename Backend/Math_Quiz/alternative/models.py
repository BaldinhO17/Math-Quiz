from django.db import models

# Create your models here.
class Alternative(models.Model):
    text = models.TextField()
    isCorrect = models.BooleanField()

    def __str__(self):
        return self.text

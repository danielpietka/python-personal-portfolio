from django.db import models
from django.db.models.fields import CharField, DateField

class Blog(models.Model):
    title = CharField(max_length=200)
    date = DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
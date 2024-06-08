from django.db import models

# Create your models here.
class studinfo(models.Model):
    title = models.CharField(max_length=100)
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(max_length=100,)
    style = models.CharField(max_length=100,)
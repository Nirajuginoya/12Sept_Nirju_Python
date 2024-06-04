from django.db import models

# Create your models here.

class booklist(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    isbn=models.BigIntegerField()
    publisher=models.CharField(max_length=50)
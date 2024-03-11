from django.db import models

class Author(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()

class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')
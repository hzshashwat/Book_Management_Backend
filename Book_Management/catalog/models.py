from django.db import models
from django.core.validators import  MaxLengthValidator,  MinLengthValidator, MinValueValidator

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length = 200)
    isbn_no = models.CharField('ISBN', unique = True, primary_key = True, max_length = 13, validators=[ MaxLengthValidator(13 , message="As per ISBN standard, all ISBNs are 13-digits long."), MinLengthValidator(13, message="As per ISBN standard, all ISBNs are 13-digits long.")])
    author_name = models.CharField(max_length = 150)
    genre = models.CharField(max_length = 100)
    inventory = models.IntegerField(default = 0, validators=[ MinValueValidator(0)])
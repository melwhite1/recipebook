from django.db import models
from django.shortcuts import reverse

class Recipe(models.Model):
    name= models.CharField(max_length=120)
    cooking_time= models.PositiveIntegerField(help_text= 'in minutes')
    ingredients= models.CharField(max_length=250)
    difficulty= models.CharField(max_length=20)
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse ('recipes_home:detail', kwargs={'pk': self.pk})

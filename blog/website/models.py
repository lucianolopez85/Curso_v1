from django.db import models

class Category(models.TextChoices):
    TECH = 'TC','Tecnologia'
    CR = 'CR','Curiosidade'
    GR = 'GR', 'Geral'

    
class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.CharField(
        max_length=2,
        choices=Category.choices,
        default=Category.GR,
    )  


    def __str__(self):
        return self.title


    #def full_name(self):    => função que junta os titulos
     #   return self.title + self.sub_title 

    categories.admin_order_field = 'categories'
    
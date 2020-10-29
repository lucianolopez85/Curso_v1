from django.db import models

class Category(models.TextChoices):
    TECH = 'TC','Tecnologia'
    CR = 'CR','Curiosidade'
    GR = 'GR', 'Geral'

class Contact(models.Model):
    name_contact = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name_contact  # mostra o nome no admin
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.CharField(
        max_length=2,
        choices=Category.choices,
        default=Category.GR,
    )  

    imagem = models.ImageField(upload_to = 'posts', null=True, blank=True)


    def __str__(self):
        return self.title


    #def full_name(self):    => função que junta os titulos
     #   return self.title + self.sub_title 

    categories.admin_order_field = 'categories'
    
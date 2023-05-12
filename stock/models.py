from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title
    
class Products(models.Model):
    name = models.CharField(max_length=40)

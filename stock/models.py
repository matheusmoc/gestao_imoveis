from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title
    
class Product(models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    qty = models.FloatField()
    purchase_price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self) -> str:
        return self.name
    
    def discount(self, discount): #valor de venda - o valor do desconto = valor atual do produto
        return self.sale_price - ((self.purchase_price * discount) / 100)

    def profit(self): #lucro da venda menos a compra em porcentagem
        profit = self.sale_price - self.purchase_price
        return (profit * 100) / self.purchase_price
    

class ProductImage(models.Model):
    image = models.ImageField(upload_to="product_image")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
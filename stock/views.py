from django.shortcuts import render
from .models import Category, Product, ProductImage
from django.http import HttpResponse
from PIL import Image, ImageDraw
from datetime import date
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

def add_product(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, 'add_product.html', {"categories": categories})
   
    elif request.method == "POST":
        name = request.POST.get('name')
        category = request.POST.get('category')
        qty = request.POST.get('qty')
        purchase_price = request.POST.get('purchase_price')
        sale_price = request.POST.get('sale_price')
        images = request.FILES.getlist('images')
        
        product = Product(
            category_id=category, 
            name=name, 
            qty=qty, 
            purchase_price=purchase_price, 
            sale_price=sale_price, 
        )
        
        product.save()

        for f in images:
  
        #    img = ProductImage(image = f, product=product)
        #    img.save()

           name = f'{date.today()}-{product.id}.jpg'
           img = Image.open(f) #abrir imagem com o pillow
           img = img.convert('RGB') #padrão RGB
           img = img.resize((300, 300)) #redimensionar
           draw = ImageDraw.Draw(img) #marca d'agua
           draw.text((20, 280), f"Gestão imóveis {date.today()}", (255,255,255))
           
           output = BytesIO()
           img.save(output , format="JPEG", quality=100)
           output.seek(0) #volta o ponteiro para o começo do arquivo
           img_final = InMemoryUploadedFile(output, "ImageField",name, "image/jpeg", sys.getsizeof(output), None) #salva no disco
           
           img_main = ProductImage(image=img_final, product=product)
           img_main.save()
    return HttpResponse('Enviado')
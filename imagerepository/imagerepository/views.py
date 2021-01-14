from django.db.models.fields import DateField
from django.shortcuts import get_object_or_404, redirect, render
from .models import ImageRepository

def displayImages(request):
    allImages = ImageRepository.objects.all()
    return render(request, 'index.html', {'ImageRepository': allImages})

def editImages(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        desc = request.POST['description']
        price = request.POST['price']
        uploadedImage = request.FILES['uploadedImg']
        
        ins = ImageRepository(title=title, description=desc, user='shopify2021', price=price, image=uploadedImage)
        ins.save()

    allImages = ImageRepository.objects.all()
    return render(request, 'edit.html', {'ImageRepository': allImages})

def deleteImage(request, id=None):
    ins = get_object_or_404(ImageRepository, id=id)
    ins.delete()
    
    return redirect("editImages")
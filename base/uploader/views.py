from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def uploader(request):
    queryset = ImageUpload.objects.all()

    if request.method == 'POST':

        image = request.FILES.get('image')

        print("image:", image )  # Add this line for debugging

        ImageUpload.objects.create(
            image = image,
        )
        messages.success(request, "Image uploaded succefully!!")
        return redirect('/')

    context = {'images': queryset}
    return render(request, "home.html", context)

def update(request, id):
    queryset = ImageUpload.objects.get(id=id)

    if request.method == 'POST':

        image = request.FILES.get('image')

        if image:
            queryset.image = image

        queryset.save() 
        messages.info(request, "Image updated succefully!!")
        return redirect("/")

    context = {'images': queryset}
    return render(request, "update.html", context)

def delete(request, id):
    queryset = ImageUpload.objects.get(id=id) 
    queryset.delete()
    messages.warning(request, "Image deleted succefully!!")
    return redirect('/')
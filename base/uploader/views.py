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
        messages.success(request, "Receipes added succefully!!")
        return redirect('/')

    context = {'images': queryset}
    return render(request, "base.html", context)
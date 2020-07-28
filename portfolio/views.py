from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'portfolio/index.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

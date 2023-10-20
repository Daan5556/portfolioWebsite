from django.shortcuts import render
from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def aboutme(request):
    return render(request, 'aboutMe.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')



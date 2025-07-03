from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request , "index.html")


def newlineremover(request):
    return HttpResponse("New Line Remover")

def removepunc(request):
    return HttpResponse("Remove Punctuation")

def spaceremover(request):
    return HttpResponse("Space Remover")
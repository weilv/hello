from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index1(request):
    # return HttpResponse("hello world")
    return render(request, 'index.html', {'hello':'hello,blogs!!!'})

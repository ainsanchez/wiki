from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

#To render an entire HTML page
def index(request):
    return render(request, "wiki/index.html")

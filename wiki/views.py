from django.shortcuts import render
from django.shortcuts import HttpResponse

from encyclopedia import util

# Create your views here.

#To render an entire HTML page
def index(request):
    return render(request, "wiki/index.html")

def title(request, name):
    return render(request, "wiki/title.html", { 
      "name": util.get_entry(name),
      "title": name
    })

from django.shortcuts import render, redirect

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, name):
    return render(request, "wiki/title.html", { 
      "name": util.get_entry(name),
      "title": name
    })

def search(request):
    term = request.POST.get('q', 'notfound')
    return redirect('title', name=term)

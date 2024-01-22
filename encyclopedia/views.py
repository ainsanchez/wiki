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
    if (util.get_entry(term) != None):
        return redirect('title', name=term)
    else:
        return render(request, "encyclopedia/search_results.html", {
            "new_entries": util.get_entry_subs(term)
        })
    
def create(request):
    return render(request, "encyclopedia/create_entry.html")

from django.shortcuts import render

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

def results(request):
    inp_value = request.GET.get('text', 'This is a default value')
    context = {'inp_value': inp_value}
    return render( request, 'results.html', context)
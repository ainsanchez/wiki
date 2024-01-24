from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from . import util

class NewTaskForm(forms.Form):
    title = forms.CharField(label="Title")
    text = forms.CharField(label="Content",
                           widget=forms.Textarea(attrs={"rows":"5"}))


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
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            text = form.cleaned_data["text"]
            if title not in util.list_entries():
                util.save_entry(title, text)
                return HttpResponseRedirect(reverse("title", args=(title,)))
            else:
                return HttpResponse("Error: Title already exists")
        else:
            return render(request, "encyclopedia/index.html", {
                "form": form
            })
    return render(request, "encyclopedia/create_entry.html", {
        "form": NewTaskForm()
    })    

    

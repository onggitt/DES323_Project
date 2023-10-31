from django.shortcuts import render

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def comment_index(request):
    context = {}
    return render(request, "components/comments.html", context=context)
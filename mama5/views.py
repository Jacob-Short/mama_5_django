from django.shortcuts import render

def index_view(request):
    context = {}
    return render(request, 'index.html', context)


def about_view(request):
    context = {}
    return render(request, 'about.html', context)

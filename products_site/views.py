from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def sent(request):
    return render(request, 'contact/sent.html')
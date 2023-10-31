from django.shortcuts import render

app_name = 'core'

def index(request):
    return render(request, 'index.html')
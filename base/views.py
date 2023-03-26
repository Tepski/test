from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'base/home.html')    

def page2(request):
    return render(request, 'base/page2.html')

def page3(request):
    return render(request, 'base/page3.html')
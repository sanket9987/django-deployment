from django.shortcuts import render

# Create your views here.

def relative(request):
    return render(request,'basicapp/relative_url.html')

def index(request):
    return render(request,'basicapp/index.html')

def other(request):
    d = {'dict' : "I'm the best in the world"}
    return render(request,'basicapp/other.html',context = d)

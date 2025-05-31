from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def fun(request):
    return render(request, "core/fun.html")
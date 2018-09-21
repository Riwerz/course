from django.shortcuts import render

# Create your views here.
def load_mainpage(request):
    return render(request, 'mainpage.html')

def load_login(request):
    return render(request, 'mainpage.html')
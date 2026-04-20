from django.shortcuts import render

def home(request):
     return render(request, 'home/index.html')
def about(request):
        return render(request, 'home/about.html')
def contact(request):
        return render(request, 'home/contact.html')
def home_page(request):
        return render(request, 'home/home.html')
# Create your views here.
def index(request):
        return render(request, 'index.html')
from django.shortcuts import render

# Create your views here.
def home(request):
    data = {"title": "Home Page Django", "content": "Welcome to the amazing Django course!"}
    context = {
        "data": data,
    }
    return render(request, 'app_001/home.html', context)

def about(request):
    return render(request, 'app_001/about.html')
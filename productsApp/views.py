from django.shortcuts import render

# Create your views here.
def home(request):
    context ={}
    return render(request,'productsApp/home.html' , context)
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import MountainForm
# Create your views here.

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try: 
            user = User.objects.get(username = f"_{username}")
        except:
            print('User not found!') # flash  messages
        
        user = authenticate(request, username=username, password=password)

        if user is not None: 
            login(request, user)
            return redirect('home')
        else:
            print('Wrong Credentials!')
    context = {}
    return render(request, 'authApp/login_form.html', context)

def logoutUser(request):
    context ={}
    logout(request)
    return redirect('login')

def registerUser(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # pausing creation
            user.username = f"_{user.username.lower()}" # formating
            user.save() # svaes in DB
            login(request, user)
            return redirect('home')

    context ={"form":form}
    return render(request, 'authApp/register_form.html', context)

# we restrict access

@login_required(login_url='login')
def createMountain(request):
    form = MountainForm()

    if request.method == "POST":
        form = MountainForm(request.POST) # gets the data from what the user has input
        if form.is_valid():
            form.save()
            return redirect("readMountains")
            
    context = {"form": form}
    return render(request, "authApp/form.html", context)

@login_required(login_url='login')
def readMountains(request):

    """
    - fetch data from DB
    - save data in context
    - pass data to template
    """

    mountains = Mountain.objects.all()
    context ={"mountains":mountains}
    return render(request, "authApp/mountains.html", context)

@login_required(login_url='login')
def readOneMountain(request, pk):
    mountain = Mountain.objects.get(id = pk)
    context ={"mountain":mountain}
    return render(request,"authApp/mountain.html", context)

@login_required(login_url='login')
def updateMountain(request,pk):
    """
    - fetch the mountain details
    - create the mountain form instance
    - pass the instance of the mountain to the mountain form
    - update mountain
    """
    mountain = Mountain.objects.get(id = pk )
    form = MountainForm(instance = mountain)

    if request.method == "POST":
        form = MountainForm(request.POST, instance= mountain)
        if form.is_valid():
            form.save()
            return redirect("readMountains")

    context = {"form": form}
    return render(request, "authApp/form.html", context)

def deleteMountain(request, pk):
    mountain = Mountain.objects.get(id = pk)

    if request.method == "POST":
        mountain.delete()
        return redirect("readMountains")
    context ={"mountain":mountain}
    return render(request, "authApp/delete.html", context)

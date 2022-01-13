from django.shortcuts import redirect, render
from .forms import UserCreationForms, UserAutenticationForm
from django.contrib.auth import authenticate, login
# Create your views here.

def homeUserLogin(request):
    form = UserAutenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        user = authenticate(username=user, password=password)
        if user is not None:
            login(request, user)
            return redirect("ListarContato")
    return render(request,'index.html',{'form':form})


def createUser(request):
    form = UserCreationForms(request.POST or None)
    if form.is_valid():
        form.save()

        #autentic
        user = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password2")

        user = authenticate(username=user, password=password)
        if user is not None:
            login(request, user)
            return redirect("ListarContato")
    return render(request,'create.html',{'form':form})
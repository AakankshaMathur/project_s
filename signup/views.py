from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'index.html')

def user_register(request):
    # if request.user.is_authenticated:
        # return redirect('/home')
    
    if request.method=='POST':
        regForm=UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            email = regForm.cleaned_data['email']
            password = regForm.cleaned_data['password']
            user = authenticate(email = email,password = password)
            login(request, user)
            return redirect('/home')
        else:
            return render(request, 'registration/register.html', {'form':form})
    else:
            form = UserCreationForm()
            # messages.success(request, 'User has been registered')
    return render(request, 'registration/register.html', {'form':form})


def user_login(request):

    # if request.user.is_authenticated:
        # return redirect('/home')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
 
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            form = AuthenticationForm()
            return render(request,'registration/login.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('/login')
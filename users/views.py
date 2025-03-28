from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import CustomUserCreationForm, UserLoginForm
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('task_list')
        
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username  = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('task_list')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')



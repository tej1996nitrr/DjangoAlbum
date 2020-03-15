from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    print("REG")
    if request.method == 'POST':
        print("POST")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
            messages.success(request, f'Your account is created.Please login.')

            return redirect('login')
        else:
            print("not valid")
    else:
        form = UserRegisterForm()
        
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    
    return render(request,'users/profile.html')
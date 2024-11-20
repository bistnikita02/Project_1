from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login

#from .forms import CompanyregistrationForm

def register(request):
    if request.method == 'POST':
        profile = UserProfileForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid() and profile.is_valid():
            user = form.save()
            profile.instance.user = user
            userprofile = profile.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username = username,password = password)
            if user is not None:
                login(request,user)

            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('home')
    else:
        form = UserRegisterForm()
        profile = UserProfileForm()
    return render(request, 'users/register.html', {'form':form,'profile':profile})
 

@login_required
def profile(request):
    if request.method =="POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account hs been updated!')

    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form':u_form,
            'p_form':p_form

        }    
        return render(request,'users/profile.html', context)
        
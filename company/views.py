from django.shortcuts import render, redirect
from  .forms import CompanyRegisterForm, CompanyProfileForm
from django.contrib import messages
 
def register(request):
    if request.method == 'POST':
        profile = CompanyProfileForm(request.POST)
        form = CompanyRegisterForm(request.POST)
        if form.is_valid():
            company = form.save()
            companyprofile = profile.save(commit= False)
            companyprofile.company = company
            companyprofile.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
        
    else:     
        form = CompanyRegisterForm()
        profile = CompanyProfileForm()
    return render(request, 'company/register.html', {'form': form, 'profile':profile})



from django.shortcuts import render, redirect
from .forms import UserRegistration, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}, please log in!')
            return redirect('shop-registration')
        
    else:
        form = UserRegistration()
    return render(request, 'customers/registration.html', {'form':form}) 

@login_required
def shop_profile(request):  
    if request.method == POST:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
        
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'customers/customer-profile.html', context)

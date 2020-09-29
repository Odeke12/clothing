from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)#instance of the form
        if form.is_valid():#back end validation done by django with usercreation form
            form.save() 
            username = form.cleaned_data.get('username') #the validated data will be in the form.cleaned dictionary
            messages.success(request,f'Your new account has been created! You can now log in')
            return redirect('login')
    else: 
        form = UserRegisterForm() #instantiates an empty form for anything without post
            
    return render(request,'users/register.html', {'form':form}) #request,template,context to the template  

@login_required #adds functionality to profile
def profile(request): 
    if request.method == 'POST': #when our form is submitted, this is what is run
        u_form = UserUpdateForm(request.POST, instance=request.user) #request.post passes in the submitted data
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') 
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile) 
      
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request,'users/profile.html',context)
    
 
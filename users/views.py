from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login 
from .forms import LoginForm

def user_login(request): 
    if request.method == 'POST': #If from has been submitted
        form = LoginForm(request.POST) # A fprm bound to the POST data
        if form.is_valid(): #All validation rule pass
            cd = form.cleaned_data
            user = authenticate(request,
                                    username=cd['username'],
                                    password=cd['password1'])
    else:
        form = LoginForm()
    return render(request, 'users/register.html', {'form': form})
        



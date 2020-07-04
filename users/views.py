from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages


from .models import Profile
from .forms import UserRegisterForm, ProfileForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created! {username} can now login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def profile(request, username):
    qs = Profile.objects.filter(user__username=username)
    if not qs.exists():
        raise Http404
    profile_obj = qs.first()
    context = {
        "username": username,
        "profile": profile_obj
    }
    return render(request, 'users/profile.html', context)


def profile_update_view(request):
    if not request.user.is_authenticated: # is_authenticated()
        return redirect("/login?next=/profile/update")

    user = request.user
    my_profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST or None, instance=my_profile)
        if form.is_valid():
            profile_obj = form.save(commit=False)
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            profile_obj.save()
            messages.success(request, f'Account has been edit!')
            return redirect('home')
    else:
        form = ProfileForm()

    context = {
        "form": form,
        "btn_label": "Save",
        "title": "Update Profile"
    }
    return render(request, "users/edit_profile.html", context)

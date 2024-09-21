from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Profile
from .forms import CustomUserCreationForm


def login_user(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'users/login-register.html', {'page': page})


def logout_user(request):
    messages.info(request, 'User was logged out')
    logout(request)
    return redirect('login')


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower().strip()
            user.save()

            messages.success(request, 'User account was created')

            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request,
                           'An error has occoured during registration')


    context = {'page': page, 'form': form}
    return render(request, 'users/login-register.html', context)


def profiles(request):
    profiles = Profile.objects.all()

    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)

    top_skills = profile.skill_set.exclude(description__exact='')
    other_skills = profile.skill_set.filter(description='')

    context = {'profile': profile,
               'top_skills': top_skills,
               'other_skills': other_skills,}

    return render(request, 'users/user-profile.html', context)


@login_required(login_url='login')
def account_user(request):
    profile = request.user.profile

    context = {'profile': profile}
    return render(request, 'users/account.html', context)
from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,
    )

from django.shortcuts import render, redirect

from .forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from .models import Profile

# Create your views here.
def login_view (request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated())
        if next:
            return redirect(next)
        return redirect("/")


    return render(request, "login.html",{"form":form, "title":title})

def register_view (request):
    if request.method == 'POST':
        print(request.user.is_authenticated())
        next = request.GET.get('next')
        title = "Register"
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password")
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)
            return redirect('profile')
    else:
        form = UserRegisterForm(request.POST or None)
        title = "Register"
    return render(request, "register.html", {
        'form': form,
        'title': title
        })

def logout_view(request):
    logout(request)
    return redirect("/")

def profile_edit (request):
    if request.method == 'POST':
        title = "Profile"
        profile_form = UserProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect("/")
    else:
        profile_form = UserProfileForm(instance = request.user.profile)
        title = "Profile"
    return render(request, "profile.html", {
        'title': title,
        'profile_form': profile_form
        })

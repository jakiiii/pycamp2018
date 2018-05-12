from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

from .forms import IndividualSignUpForm, OrganizationSignUpForm, SignInForm


# redirect logged in user to home
def redirect_authenticated_user(user):
    if user.is_authenticated:
        return redirect('home')


def home(request):
    return render(request, 'home.html')


# @user_passes_test(redirect_authenticated_user)
def individual_signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = IndividualSignUpForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('userprofile:create_profile'))

    form = IndividualSignUpForm()
    return render(request, 'auth/signup.html', {'form': form})


def organization_signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = OrganizationSignUpForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # return redirect('organization_signup')
            return HttpResponse('<h1>This is Organization Profile creation form</h1>')

    form = OrganizationSignUpForm()
    return render(request, 'auth/signup.html', {'form': form})


# @user_passes_test(redirect_authenticated_user)
def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    form = SignInForm()
    return render(request, 'auth/signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('home')


def password_change(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        form = PasswordChangeForm(request.user)
        return render(request, 'auth/password_change.html', {'form': form})


def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                from_email='from@example.com',
                email_template_name='registration/password_reset_body.html'
            )
            return redirect('home')
    form = PasswordResetForm(None)
    return render(request, 'auth/password_reset.html', {'form': form})
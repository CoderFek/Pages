from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomSignupForm, CustomLoginForm, ChangePasswordForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User




# Create your views here.
@login_required
def homeview(request):
    username = request.user.username
    return render(request, 'pages/home.html', {'username':username})


@login_required
def profileview(request):
    username = request.user.username
    email = request.user.email
    date_joined = request.user.date_joined
    last_active = request.user.last_login

    context = {
        'username':username,
        'email':email,
        'date_joined':date_joined,
        'last_active':last_active
    }

    return render(request, 'pages/profile.html', context)


@login_required
def password_change(request):
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password changed successfully!")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below")
    else:
        form = ChangePasswordForm(user=request.user)
    return render(request, 'pages/change_password.html', {'form':form})



def loginview(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")

    else:
        form = CustomLoginForm()
    return render(request, 'pages/login.html', {'form':form})


def logoutview(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')


def signupview(request):
    if request.method == 'POST':
        form = CustomSignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the following errors.")
    else:
        form = CustomSignupForm()
    return render(request, 'pages/signup.html', {'form':form})


def forgot_password_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email=email).first()

            if user:
                form.save(
                    request=request,
                    email_template_name='pages/password_reset_email.html',
                )
                messages.success(request, "A password reset link has been sent to your email address.")
                return redirect('login')
            else:
                messages.error(request, "No user found with this email address.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PasswordResetForm()

    return render(request, 'pages/forgot_password.html', {'form':form})


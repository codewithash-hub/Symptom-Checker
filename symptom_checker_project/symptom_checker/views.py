from django.shortcuts import render, redirect
from django.http import JsonResponse
from .nlp_model import diagnose_symptoms
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, LoginForm

def home(request):
    return render(request, 'symptom_checker/home.html')

def treatment_plan(request):
    return render(request, 'treatment_plan.html')

def check_symptoms(request):
    if request.method == 'POST':
        symptoms = request.POST.get('symptoms')
        diagnosis = diagnose_symptoms(symptoms)
        return JsonResponse({'diagnosis': diagnosis})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login =(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'symptom_checker/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'symptom_checker/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')
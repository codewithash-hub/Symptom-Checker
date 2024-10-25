from django.shortcuts import render, redirect
from django.http import JsonResponse
from .nlp_model import diagnose_symptoms
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, LoginForm
from .models import Interaction, FAQ
from .nlp_model import diagnose_symptoms
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.template import TemplateDoesNotExist

def home(request):
    return render(request, 'symptom_checker/home.html')

def treatment_plan(request):
    return render(request, 'treatment_plan.html')

@login_required  # Ensures only logged-in users can access this view
def check_symptoms(request):
    if request.method == 'POST':
        symptoms = request.POST.get('symptoms')
        # Diagnose based on symptoms
        diagnosis = diagnose_symptoms(symptoms)
        # Save the interaction to the database, linking it to the logged-in user
        Interaction.objects.create(
            user=request.user,
            user_input=symptoms,
            ai_response=diagnosis
        )
        return JsonResponse({'diagnosis': diagnosis})
    return JsonResponse({'error': 'Invalid request'}, status=400)

# retrieve and display the interactions for the currently logged-in user
@login_required
def user_interactions(request):
    interactions = Interaction.objects.filter(user=request.user)
    try:
        template = get_template('symptom_checker/interactions.html')
    except TemplateDoesNotExist:
        print("Template not found: symptom_checker/interactions.html")
    return render(request, 'symptom_checker/interactions.html', {'interactions': interactions})

def interactions_view(request):
    user_name = request.user.username
    context = {
        'user_name': user_name,
    }
    return render(request, 'symptom_checker/interactions.html', context)

def faq_view(request):
    faqs = FAQ.objects.all() 
    return render(request, 'home.html', {'faqs': faqs})


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
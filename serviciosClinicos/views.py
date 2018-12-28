from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.

def bienvenida(request):
    return render(request, 'bienvenida.html')

def registro(request):
    return render(request, 'registration/login.html')

@login_required()
def base(request):
    return render(request, 'baseAdmin.html')

def baseNormal(request):
    return render(request, 'base.html')
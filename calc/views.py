from django.forms.models import model_to_dict
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

from django.views.generic import CreateView
from .forms import CustomUserCreationForm



class MyLoginView(LoginView):
    template_name = 'calc/login.html'

# Create your views here.

def index(request):
    return render(request, 'calc/index.html', {})


class MyRegister(CreateView):
    template_name = 'calc/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('calc:index')


@login_required
def user_logout(request):
    logout(request)
    return reverse_lazy('calc:index')

def register(request):
    pass
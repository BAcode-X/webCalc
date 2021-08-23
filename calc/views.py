from django.http import request
import calc
from django.forms.models import model_to_dict
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, ListView, UpdateView
from .forms import CustomUserCreationForm, UserChangeForm
from .models import History

USER = get_user_model()

# Create your views here.

def index(request):
    return render(request, 'calc/index.html', {})


class MyLoginView(LoginView):
    template_name = 'calc/login.html'

class MyRegister(CreateView):
    template_name = 'calc/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('calc:index')

class ListHistory(LoginRequiredMixin, ListView):
    model = History
    template_name = 'calc/history.html'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class Calculate(LoginRequiredMixin, CreateView):
    model = History
    fields = ['expression']

    template_name = 'calc/calculate.html'

    def form_valid(self, form):
        history = History()
        print(form)
        history.expression = form.cleaned_data.get('expression')
        try:
            history.result = str(eval(history.expression))
        except:
            history.result = None
        history.user = self.request.user
        history.save()
        return render(self.request, 'calc/calculate.html', {
            'expression': history.expression,
            'result': history.result or "Undefined!"
            })

class ChangeProfile(UpdateView):
    model = USER
    fields = ['nick', 'email','first_name', 'last_name',]
    # form_class = UserChangeForm
    # pk_url_kwarg = "pk"
    template_name = 'calc/profile.html'
    success_url = reverse_lazy('calc:index')
    
    def get_object(self, *args):
        return self.model.objects.filter(id=self.request.user.pk).first()
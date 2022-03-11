from dataclasses import fields
from re import template
from django.shortcuts import render
from django.contrib.auth import authenticate, login as do_login
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import UserCreationFormWithEmail , ProfileForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

class LoginView(TemplateView):
    
    template_name = "registration/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.add_message(request, messages.WARNING, 'El usuario no existe')
                return HttpResponseRedirect(reverse('user_login'))

        else:
            messages.add_message(request, messages.WARNING, 'Datos inválidos')
            return HttpResponseRedirect(reverse('user_login'))

def logout_view(request):
    logout(request)
    messages.add_message(request, messages.WARNING, 'Nos vemos pronto')
    return HttpResponseRedirect(reverse('user_login'))


class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('user_login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('user_login') + '?register'

@method_decorator(login_required,name='dispatch')
class ProfileUpdate(UpdateView):

    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
         profile,created =Profile.objects.get_or_create(user=self.request.user)
         return profile

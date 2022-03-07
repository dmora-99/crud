from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login as do_login
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import logout

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
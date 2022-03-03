from pyexpat import model
from sre_constants import SUCCESS
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse , reverse_lazy
from django.views.generic.edit import CreateView , UpdateView , DeleteView

# Create your views here.

class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

class PageCreateView(CreateView):
    model = Page
    fields = ['title','content','order']
    success_url = reverse_lazy ('pages:pages')


class PageUpdateView(UpdateView):
    model = Page
    fields = ['title','content','order']
    template_name_suffix = '_update_form'
    

    def get_success_url(self):
        return reverse_lazy('pages:updated', args=[self.object.id]) + '?ok'



from pyexpat import model
from sre_constants import SUCCESS
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse , reverse_lazy
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from .forms import PageForm
from django.shortcuts import redirect

class StaffRequiredMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request , *args , **kwargs )

# Create your views here.

class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

class PageCreateView(StaffRequiredMixin ,CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy ('pages:pages')


class PageUpdateView(StaffRequiredMixin ,UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'
    

    def get_success_url(self):
        return reverse_lazy('pages:updated', args=[self.object.id]) + '?ok'

class PageDeleteView(StaffRequiredMixin,DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')




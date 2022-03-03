from django.urls import path
from . import views
from .views import PageCreateView, PageDetailView, PageListView , DetailView

pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:page_slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreateView.as_view(), name='create'),
],'pages')


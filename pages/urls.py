from django.urls import path
from . import views
from .views import PageCreateView, PageDetailView, PageListView , DetailView , PageUpdateView , PageDeleteView

pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:page_slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreateView.as_view(), name='create'),
    path('update/<int:pk>/', PageUpdateView.as_view(), name='updated'),
    path('delete/<int:pk>/', PageDeleteView.as_view(), name='deleted'),
],'pages')


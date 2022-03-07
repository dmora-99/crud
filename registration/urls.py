from django.urls import path
from .views import *
urlpatterns = [
    path('login/', LoginView.as_view(), name='user_login'),
    path('logout/', logout_view, name='user_logout'),
]
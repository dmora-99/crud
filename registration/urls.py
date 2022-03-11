from django.urls import path
from .views import *
urlpatterns = [
    path('login/', LoginView.as_view(), name='user_login'),
    path('logout/', logout_view, name='user_logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
]

from django.urls import path, include
from .views import RegisterView, LoginView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('Login', LoginView.as_view()),
]

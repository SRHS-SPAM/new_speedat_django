from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView

urlpatterns = [
    path('register', RegisterView.as_view()),   #회원가입 엔드포인트
    path('login', LoginView.as_view()),         #로그인 엔드포인트
    path('user', UserView.as_view()),           #사용자 정보 및 조회 엔드포인트
    path('logout', LogoutView.as_view()),       #로그아웃 엔드포인트
]

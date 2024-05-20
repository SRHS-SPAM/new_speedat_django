from django.urls import path, include
from .views import RegisterView, LoginView, UserView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register', RegisterView.as_view()),   # 회원가입 엔드포인트
    path('login', LoginView.as_view()),         # 로그인 엔드포인트
    path('user', UserView.as_view()),           # 사용자 정보 및 조회 엔드포인트
    path('logout', LogoutView.as_view()),       # 로그아웃 엔드포인트

    # OAuth 및 JWT 관련 엔드포인트 추가
    path('accounts/', include('allauth.urls')),  # allauth 경로 추가
    path('auth/', include('dj_rest_auth.urls')),  # dj-rest-auth 경로 추가
    path('auth/registration/', include('dj_rest_auth.registration.urls')),  # 회원가입 경로 추가
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT 토큰 발급
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT 토큰 갱신
]

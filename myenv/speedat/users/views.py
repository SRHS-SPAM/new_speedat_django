from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt, datetime

# Create your views here.
class RegisterView(APIView):            #View 생성
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        #요청 데이터에서 이메일과 비밀번호를 불러옴
        email = request.data['email']
        password = request.data['password']

        # 이메일로 사용자를 조회
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found!')

        # 비밀번호가 일치하는지 확인합니다.
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        # JWT 토큰에 포함할 payload를 생성
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        # JWT 토큰을 생성합니다.
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response

class UserView(APIView):
    def get(self, request):
        #cookie에서 JWT토큰 가져오기
        token = request.COOKIES.get('jwt')

        if not token:
            #토큰이 없는 경우 예외처리
            raise AuthenticationFailed('Unauthenticated!')
        try:
            #JWT 토큰을 디코드하여 페이로드를 가져옵니다.
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            #토큰이 만료되었을 경우 예외 처리
            raise AuthenticationFailed('Unauthenticated!')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            raise AuthenticationFailed('User not found!')

        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','password']       #직렬화시킬 필드 목록
        extra_kwargs = {
            'password': {'write_only': True}            #비밀번호 필드는 쓰기 전용으로 설정
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None) #유효성 검사된 데이터에서 비밀번호를 제거
        instance = self.Meta.model(**validated_data)    #나머지 데이터로 사용자 인스턴스를 생성
        if password is not None:
            instance.set_password(password)             #비밀번호를 해시하여 설정
        instance.save()                                 #사용자 인스턴스를 저장
        return instance                                 #생성된 사용자 인스턴스를 반환
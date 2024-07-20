from djoser.serializers import UserCreateSerializer as BaseUserSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from .models import CustomUser

class UserCreateSerializer(BaseUserSerializer):
    class  Meta:
        model = CustomUser
        fields = ['id','first_name', 'last_name', 'username', 'email', 'password']

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'first_name', 'last_name', 'username', 'email']
        
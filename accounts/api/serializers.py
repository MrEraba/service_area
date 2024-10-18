from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


USER_MODEL = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = USER_MODEL
        fields = ['username', 'email']

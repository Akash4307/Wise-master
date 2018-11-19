from rest_framework import serializers
from .models import UserInfo

class json(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('UserName', 'UserBookLogo')
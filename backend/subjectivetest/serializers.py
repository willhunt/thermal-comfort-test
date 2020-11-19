from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import (
    TestModel,
    OccupantModel,
    BodyZoneModel,
    PresetZonesModel,
    GlobalResponseModel,
    LocalResponseModel,
    ProfileModel
)

class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'


class BodyZoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BodyZoneModel
        fields = '__all__'


class OccupantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OccupantModel
        fields = '__all__'


class PresetZonesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PresetZonesModel
        fields = '__all__'


class GlobalResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GlobalResponseModel
        fields = '__all__'


class LocalResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LocalResponseModel
        fields = '__all__'

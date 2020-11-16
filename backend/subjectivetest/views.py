from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import (
    UserSerializer, GroupSerializer,
    OccupantSerializer,
    BodyZoneSerializer,
    PresetZonesSerializer,
    GlobalResponseSerializer,
    LocalResponseSerializer
)
from .models import (
    TestModel,
    OccupantModel,
    BodyZoneModel,
    PresetZonesModel,
    GlobalResponseModel,
    LocalResponseModel,
    ProfileModel
)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # authentication_class = [JSONWebTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class OccupantViewSet(viewsets.ModelViewSet):
    queryset = OccupantModel.objects.all()
    serializer_class = OccupantSerializer
    permission_classes = [permissions.IsAuthenticated]


class BodyZoneViewSet(viewsets.ModelViewSet):
    queryset = BodyZoneModel.objects.all()
    serializer_class = BodyZoneSerializer
    permission_classes = [permissions.IsAuthenticated]


class PresetZonesViewSet(viewsets.ModelViewSet):
    queryset = PresetZonesModel.objects.all()
    serializer_class = PresetZonesSerializer
    permission_classes = [permissions.IsAuthenticated]


class GlobalResponseViewSet(viewsets.ModelViewSet):
    queryset = GlobalResponseModel.objects.all()
    serializer_class = GlobalResponseSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocalResponseViewSet(viewsets.ModelViewSet):
    queryset = LocalResponseModel.objects.all()
    serializer_class = LocalResponseSerializer
    permission_classes = [permissions.IsAuthenticated]
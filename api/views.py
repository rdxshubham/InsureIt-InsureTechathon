from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status, generics
from rest_framework.decorators import detail_route

from api.models import TrueCallerData
from api.serializers import TrueCallerSerializer

# Create your views here.


class TruecallerViewSet(viewsets.ModelViewSet):
    queryset = TrueCallerData.objects.all()
    serializer_class = TrueCallerSerializer
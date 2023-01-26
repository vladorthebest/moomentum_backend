from django.shortcuts import render
from rest_framework import viewsets
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.permissions import IsAuthenticated

from .serializers import LevelSerializer
from .models import Level


class LevelAPI(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            return self.queryset.get(user=self.request.user.id)
        except ObjectDoesNotExist:
            return False
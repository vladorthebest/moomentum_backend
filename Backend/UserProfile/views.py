from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .serializers import ProfileSerializer
from .models import Profile
from django.shortcuts import get_object_or_404

class ProfileAPI(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication, ]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        object = get_object_or_404(queryset, user=self.request.user.id)
        self.check_object_permissions(self.request, object)
        return object

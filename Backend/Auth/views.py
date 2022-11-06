from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .serializer import LoginSerializer, RegisterSerializer
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from rest_framework import generics

# Login user
class LoginView(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication, ]
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data, context={
                                     'request': self.request})               
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({'user': user.id})
    
class PingView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request):
        isAuth = request.user.id
        
        if isAuth:
            return Response({'userID': isAuth})
        return Response({'userID': 0})
    
class RegisterView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    def get(self, request):
        logout(request)
        return Response({'result': 1})

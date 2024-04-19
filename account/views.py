from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)
        if user:
            token = authenticate(username=username, password=password)
            return Response({'token': token})
        else:
            return Response({'error': 'Invalid credentials'})

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

class AddressableLocations(APIView):
    def get(self, request, format=None):
        
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile


class ProfileList(APIView):
    """
    List all profiles, or create a new profile.
    """
    def get(self, request):
        profiles = Profile.objects.all()
        return Response(profiles)

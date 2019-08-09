#from rest_framework import generics
from rest_framework import viewsets

from cognotest import models
from . import serializers
#from .serializers import CognoSerializer
#from .models import Cogno
from rest_framework.permissions import IsAuthenticated

# Create your viewsets here.
class CognoViewset(viewsets.ModelViewSet):
    """This class defines the viewset behavior of our rest api."""
    
    permission_classes = (IsAuthenticated,)

    queryset = models.Cogno.objects.all()
    serializer_class = serializers.CognoSerializer
'''
# Create your views here.
class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = models.Cogno.objects.all()
    serializer_class = serializers.CognoSerializer

    # def perform_create(self, serializer):
    #     """Save the post data when creating a new name."""
    #     serializer.save()
class Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Cogno.objects.all()
    serializer_class = serializers.CognoSerializer

  '''
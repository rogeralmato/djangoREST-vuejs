from rest_framework import viewsets
from realstate.models import Residence
from realstate.serializers import ResidenceSerializer

class ResidenceViewSet(viewsets.ModelViewSet):
    queryset = Residence.objects.all()
    serializer_class = ResidenceSerializer
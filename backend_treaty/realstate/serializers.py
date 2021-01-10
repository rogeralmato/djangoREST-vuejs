from rest_framework import serializers
from realstate.models import Residence

class ResidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Residence
        fields = '__all__'
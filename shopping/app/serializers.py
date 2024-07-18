from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'address', 'door_flat_no', 'phone', 'city', 'state', 'zip_code', 'image']

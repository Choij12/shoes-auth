from rest_framework import serializers
from .models import Shoes

class ShoesSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'seller', 'name', 'description', 'created_at', 'updated_at')
    model = Shoes
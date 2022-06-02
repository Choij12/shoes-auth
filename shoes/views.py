from rest_framework import generics
from .serializers import ShoesSerializer
from .models import Shoes
from .permissions import isOwnerOrReadOnly

class ShoesList(generics.ListCreateAPIView):
  permission_classes = (isOwnerOrReadOnly,)
  queryset = Shoes.objects.all()
  serializer_class = ShoesSerializer

class ShoesDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (isOwnerOrReadOnly,)
  queryset = Shoes.objects.all()
  serializer_class = ShoesSerializer
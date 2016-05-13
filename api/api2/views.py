from rest_framework import generics, viewsets
from ..models import Colors
from .serializers import ColorSerializer

class ColorListView(generics.ListAPIView):
	queryset = Colors.objects.all()
	serializer_class = ColorSerializer

class ColorDetailsView(generics.RetrieveAPIView):
	queryset = Colors.objects.all()
	serializer_class = ColorSerializer

from rest_framework.permissions import IsAdminUser

class ColorCreateView(generics.CreateAPIView):
	queryset = Colors.objects.all()
	serializer_class = ColorSerializer
	permission_classes = (IsAdminUser,)

class ColorUpdDesView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Colors.objects.all()
	serializer_class = ColorSerializer
	permission_classes = (IsAdminUser,)

#Esto es un ViewSet
class ColorViewSet	(viewsets.ModelViewSet):
	queryset = Colors.objects.all()
	serializer_class = ColorSerializer

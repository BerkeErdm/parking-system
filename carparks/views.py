from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from carparks.api.serializers import CarParksSerializer
from carparks.models import CarParks

class CarParksListAPIView(ListAPIView):
    queryset = CarParks.objects.all()
    serializer_class = CarParksSerializer

class CarParksDetailAPIView(RetrieveAPIView):
    queryset = CarParks.objects.all()
    serializer_class = CarParksSerializer
    lookup_field = 'pk' #'slug'=name

class CarParksDeleteAPIView(DestroyAPIView):
        queryset = CarParks.objects.all()
        serializer_class = CarParksSerializer
        lookup_field = 'pk'  #'slug'=name

class CarParksUpdateAPIView(UpdateAPIView):
        queryset = CarParks.objects.all()
        serializer_class = CarParksSerializer
        lookup_field = 'pk'  #'slug'=name

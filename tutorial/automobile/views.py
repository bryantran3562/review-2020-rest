from django.shortcuts import render

# Create your views here.

################################################################################
#BT - Mix in generic view. This is what rest frame work provided for you
################################################################################

from automobile.models import Person, Car
from automobile.serializers import PersonSerializer, CarSerializer
from rest_framework import generics

from snippets.permissions import IsOwnerOrReadOnly

from rest_framework import permissions


# class PersonList(generics.ListCreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer


# class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

# class CarList(generics.ListCreateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     # def perform_create(self, serializer):
#     #     serializer.save(owner=self.request.user)


# class CarDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

from rest_framework import viewsets

#BT - Understanding: Step 4: We just need to use the ViewSet to have all CRUD functionality. However, we also need to
#     configure the router. This is in snippets/urls.py. Remember, it does not matter where the
#     file is at, you just need to include it into your file and you can just use it.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


from django.shortcuts import render

# Create your views here.

################################################################################
#BT - Mix in generic view. This is what rest frame work provided for you
################################################################################

from automobile.models import Person
from automobile.serializers import PersonSerializer
from rest_framework import generics


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

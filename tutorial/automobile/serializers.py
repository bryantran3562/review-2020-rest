from os.path import abspath

from rest_framework import serializers

from automobile.models import Person, Car

#################################################################################
#BT - Using ModelSerializer class.
#################################################################################

class PersonSerializer(serializers.ModelSerializer):
    cars = serializers.RelatedField(many=True,queryset=Car.objects.all())
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'address','cars']
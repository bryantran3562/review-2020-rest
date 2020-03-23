from os.path import abspath

from rest_framework import serializers

from automobile.models import Person, Car

#################################################################################
#BT - Using ModelSerializer class.
#################################################################################

class PersonSerializer(serializers.ModelSerializer):
    cars = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'address','cars']

class CarSerializer(serializers.ModelSerializer):
    #BT - You can call your own method too.
    owner = serializers.SerializerMethodField('get_owner')

    class Meta:
        model = Car
        fields =['id','car_make','car_model','owner','person']

    def get_owner(self,obj):
        return obj.person.first_name
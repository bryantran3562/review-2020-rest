from os.path import abspath

from rest_framework import serializers

from automobile.models import Person, Car

#################################################################################
#BT - Using ModelSerializer class.
#################################################################################

# class PersonSerializer(serializers.ModelSerializer):
#     cars = serializers.StringRelatedField(many=True,read_only=True)
#     class Meta:
#         model = Person
#         fields = ['id', 'first_name', 'last_name', 'address','cars','date_service']

# class CarSerializer(serializers.ModelSerializer):
#     #BT - You can call your own method too.
#     class Meta:
#         model = Car
#         fields =['id','car_make','car_model','person']


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    #BT - This is just an additonal field that we want to display to the user to show
    #     that - This person has how many cars related. Fathter to sons.
    cars = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        #BT - Tell what model you are working with.
        model = Person
        #BT - Tell what property in our database instance to display to the user.
        fields = ['id', 'first_name', 'last_name','address','cars','url','date_service']

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        #BT - We can included these many sons (cars) that belongs to a single Father (person)
        fields =['id','car_make','car_model','person']


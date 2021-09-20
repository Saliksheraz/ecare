from django.contrib.auth.models import User
from rest_framework import serializers
from administrator.models import pharmacy, products


class pharmacySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pharmacy
        fields = '__all__'


class productsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = products
        fields = '__all__'

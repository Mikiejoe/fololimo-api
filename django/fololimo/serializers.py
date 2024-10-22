from rest_framework import serializers
from .models import Client, Tip, Transaction, Region, City, SubCounty, Weather


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class SubCountySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCounty
        fields = "__all__"


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = "__all__"

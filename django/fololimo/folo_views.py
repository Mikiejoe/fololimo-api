from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Client, Tip, Transaction, Region, City, SubCounty, Weather
from rest_framework import viewsets
from .serializers import (
    ClientSerializer, TipSerializer, TransactionSerializer, RegionSerializer,
    CitySerializer, SubCountySerializer, WeatherSerializer
)
from django.http import JsonResponse
from django.core.management import call_command


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class TipViewSet(viewsets.ModelViewSet):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def list(self, request, *args, **kwargs):
        region = get_object_or_404(Region, pk=request.query_params['region'])
        queryset = City.objects.filter(region=region)
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)


class SubCountyViewSet(viewsets.ModelViewSet):
    queryset = SubCounty.objects.all()
    serializer_class = SubCountySerializer

    def list(self, request, *args, **kwargs):
        queryset = SubCounty.objects.filter(city=request.query_params['city'])
        serializer = SubCountySerializer(queryset, many=True)
        return Response(serializer.data)


class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def retrieve(self, request, pk=None):
        city = get_object_or_404(City, pk=pk)
        queryset = get_object_or_404(Weather, city=city)
        serializer = WeatherSerializer(queryset)
        return Response(serializer.data)


def update_db(request):
    try:
        # Run the management command to update the database
        call_command('update_weather')
        return JsonResponse({"status": "success", "message": "Database updated"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})

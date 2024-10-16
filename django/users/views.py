from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.http import HttpRequest
from rest_framework.viewsets import ModelViewSet
from django.urls import reverse,resolve
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import User
from .serializers import UserDetailsSerializer
from fololimo import models as folomod
from fololimo import serializers as foloser
from insights import models as inmod
from insights import serializers as inser



@api_view(['GET'])
def test(request):
    print(reverse("rest_login")) # type: ignore
    return Response({'message': 'Hello, world!'})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_details(request:HttpRequest):
    try:
        user = request.user
        user_ser = UserDetailsSerializer(user)
        farms = inmod.Farm.objects.filter(user=user)
        farmserializer = inser.FarmSerializer(farms,many=True)
        activities = []
        for farm in farms:
            print(farm)
            activity = inser.Activity.objects.filter(farm=farm).first()
            
            if activity:
                activities.append(activity)
            
        activity_ser = inser.ActivitySerializer(activities,many=True)
        weathers = []
        for farm in farms:
            subcounty = farm.location
            county = folomod.SubCounty.objects.filter(sub_county=subcounty).first().city.city
            weather = folomod.Weather.objects.filter(city=county).first()
            if weather:
                weathers.append(weather)
            
        weather_ser = foloser.WeatherSerializer(weathers,many=True)
        data = {
            "weather": weather_ser.data,
            "profile": user_ser.data,
            "farms": farmserializer.data,
            "activities": activity_ser.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    except Exception as e:
        print(f"Error is ",str(e))
        return Response({"error":"Something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
        
    


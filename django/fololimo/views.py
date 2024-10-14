import random
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Client, Tip, Region, City, SubCounty, Weather
from .serializers import ClientSerializer, TipSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .mpesa_callback import push_stk

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]


# function to add farmers
@api_view(["POST"])
def ussd_callback(request):
    session_id = request.POST.get("sessionId")
    service_code = request.POST.get("serviceCode")
    phone_number = request.POST.get("phoneNumber")
    text = request.POST.get("text")
    user_input = text.split("*")
    cpin = None
    response = ""
    client = Client.objects.filter(phone=phone_number).first()
    
    if not client:
        client = Client(phone=phone_number)
        client.save()
    if user_input[0] == "1" and len(user_input) == 6 and user_input[1] == "1":
        client.name = user_input[5]
        client.save()
        return HttpResponse(success())
    elif user_input[0] == "2" and len(user_input) == 6 and user_input[1] == "1":
        client.name = user_input[5]
        client.save()
        return HttpResponse(success_swahili())
    if len(user_input) >= 3 and user_input[1] == "1":
        region = Region.objects.all()[int(user_input[2])-1]
        
    if len(user_input) >= 4 and user_input[1] == "1":
        counties = City.objects.filter(region=region)
        county = counties[int(user_input[3])-1]
    if len(user_input) >= 5 and user_input[1] == "1":
        sub_county = SubCounty.objects.filter(city=county)[int(user_input[4])-1]
        client.location = sub_county.sub_county
        client.save() 
    
    if text == "":
        response = index()
        return HttpResponse(response)
    elif text == "1":
        response = home()
        return HttpResponse(response)
    elif text == "2":
        response = home_swahili()
        return HttpResponse(response)
    elif text == "1*1":
        if client.location or client.name:
            response = "END You are already registered"
            return HttpResponse(response)
        response = select_region()
        return HttpResponse(response)
    elif text == "2*1":
        if client.location or client.name:
            response = "END Umeshajiandikisha!!"
            return HttpResponse(response)
        response = select_region_swahili()
        return HttpResponse(response)
    elif user_input[0] == "1" and len(user_input) == 3 and user_input[1] == "1":
        region = Region.objects.all()[int(user_input[2])-1]
        counties = City.objects.filter(region=region)
        response = select_county(counties)
        return HttpResponse(response)
    elif user_input[0] == "2" and len(user_input) == 3 and user_input[1] == "1":
        region = Region.objects.all()[int(user_input[2])-1]
        counties = City.objects.filter(region=region)
        response = select_county(counties)
        return HttpResponse(response)
    elif user_input[0] == "2" and len(user_input) == 4 and user_input[1] == "1":
        # return list of sub counties
        
        sub_counties = SubCounty.objects.filter(city=county)
        
        response = select_sub_county_swahili(sub_counties=sub_counties)
        return HttpResponse(response)
    elif user_input[0] == "1" and len(user_input) == 4 and user_input[1] == "1":
        # return list of sub counties
        
        sub_counties = SubCounty.objects.filter(city=county)
        
        response = select_sub_county(sub_counties=sub_counties)
        return HttpResponse(response)
    elif user_input[0] == "1" and len(user_input) == 5 and user_input[1] == "1":
        return HttpResponse(subscribe())
    elif user_input[0] == "2" and len(user_input) == 5 and user_input[1] == "1":
        return HttpResponse(subscribe_swahili())
    
    elif user_input[0] == "1" and len(user_input) == 2 and user_input[1] == "2":
        if client.location:
            location = client.location
        else:
            response = "END you are not registered. Please subscribe first"
            return HttpResponse(response)
        response = get_agrovet(location)
        return HttpResponse(response)
    elif user_input[0] == "2" and len(user_input) == 2 and user_input[1] == "2":
        if client.location:
            location = client.location
        else:
            response = "END Haujajiandikisha. Tafadhali jiandikise kwanza."
            return HttpResponse(response)
        response = get_agrovet_swahili(location)
        return HttpResponse(response)
    elif user_input[0] == "1" and len(user_input) == 2 and user_input[1] == "3":
        if client.location:
            location = client.location
        else:
            response = "END you are not registered. Please subscribe first"
            return HttpResponse(response)
        response = get_weather_updates(location)
        return HttpResponse(response)
    elif user_input[0] == "2" and len(user_input) == 2 and user_input[1] == "3":
        if client.location:
            location = client.location
        else:
            response = "END Haujajiandikisha. Tafadhali jiandikise kwanza."
            return HttpResponse(response)
        response = get_weather_update_swahili(location)
        return HttpResponse(response)
    elif user_input[0] == "2" and len(user_input) == 2 and user_input[1] == "4":
        response = about_swahili()
        return HttpResponse(response)
    elif user_input[0] == "1" and len(user_input) == 2 and user_input[1] == "4":
        response = about()
        return HttpResponse(response)
    elif user_input[0] == "1" and len(user_input) == 2 and user_input[1] == "5":
        response = help()
        return HttpResponse(response)
    elif user_input[0] == "2" and len(user_input) == 2 and user_input[1] == "5":
        response = help_swahili()
        return HttpResponse(response)
    response = "END Invalid choice"
    return HttpResponse(response)


def index():
    res = "CON Welcome to fololimo!!\n"
    res += "Choose a language(Chagua lugha)\n"
    res += "1. English\n"
    res += "2. Kiswahili"
    return res


def home() -> str:
    res = f"CON What do yo\n"
    res += "1. Subscribe to Fololimo.\n"
    res += "2. Get an Agrovet\n"
    res += "3. Get weather updates\n"
    res += "4. About\n"
    res += "5. Help\n"
    res += "0. Back"
    return res

def home_swahili() -> str:
    res = f"CON Unataka kufanya nini?\n"
    res += "1. Jiandikishe kwa Fololimo.\n"
    res += "2. Pata Agrovet\n"
    res += "3. Pata taarifa za hali ya hewa\n"
    res += "4. Kuhusu\n"
    res += "5. Usaidizi\n"
    res += "0. Rudi"
    return res

def subscribe() -> str:
    res = "CON Enter your name"
    return res

def subscribe_swahili() -> str:
    res = "CON Ingiza jina lako"
    return res

def get_agrovet() -> str:
    res = "CON Enter your location"
    return res

def get_agrovet_swahili() -> str:
    res = "CON Ingiza eneo lako"
    return res

def about() -> str:
    res = """
    END Fololimo is a platform that connects farmers to agrovets. Through this service, farmers can receive agricultural information through SMS, access agrovet services, and learn more about best farming practices."""
    return res

def about_swahili() -> str:
    res = """
    END Fololimo ni jukwaa linalounganisha wakulima na agrovets. Kupitia huduma hii, wakulima wanaweza kupokea taarifa za kilimo kupitia SMS, kupata huduma za agrovets, na kujifunza zaidi kuhusu mbinu bora za kilimo."""
    return res

def select_region() -> str:
    res = "CON Select your region\n"
    regions = Region.objects.all()
    i = 1
    for region in regions:
        res += f"{i}. {region.region}\n"
        i += 1
    return res

def select_region_swahili() -> str:
    res = "CON Chagua eneo lako\n"
    regions = Region.objects.all()
    i = 1
    for region in regions:
        res += f"{i}. {region.region}\n"
        i += 1
    return res

def select_county(counties) -> str:
    res = "CON Select your county\n"
    i = 1
    for county in counties:
        res += f"{i}. {county}\n"
        i += 1
    
    return res

def select_county_swahili(counties) -> str:
    res = "CON Chagua kaunti yako:\n" 
    i = 1
    for county in counties:
        res += f"{i}. {county.city}\n"
        i += 1
    return res

def select_sub_county(sub_counties) -> str:
    
    res = "CON Select your sub county:\n"
    i = 1
    for sub_county in sub_counties:
        res += f"{i}. {sub_county.sub_county}\n"
        i += 1
    return res

def select_sub_county_swahili(sub_counties) -> str:
    res = "CON Chagua eneo bunge lako:\n"
    i = 1
    for sub_county in sub_counties:
        res += f"{i}. {sub_county.sub_county}\n"
        i += 1
    return res

def get_agrovet(location) -> str:
    agrovets = Client.objects.filter(type="agrovet").filter(location=location)
    random_number = random.randint(0, len(agrovets)-1)
    
    if len(agrovets)==0:
        return "END No agrovet found in your location"
    agrovet = agrovets[random_number]
    res = f"END Agrovet: {agrovet.name} \nLocation {agrovet.location}.\n Phone: {agrovet.phone}"
    return res

def get_agrovet_swahili(location) -> str:
    agrovets = Client.objects.filter(type="agrovet").filter(location=location)
    random_number = random.randint(0, len(agrovets)-1)
    
    if len(agrovets) == 0:
        return "END Agrovet hajapatikana katika eneo lako."
    agrovet = agrovets[random_number]
    res = f"END Agrovet: {agrovet.name}\nEneo: {agrovet.location}. \nNumbari ya simu: {agrovet.phone}"
    return res

def success() -> str:
    res = "END Your subscription was successful.\n You will receive a confirmation message shortly!!"
    return res

def success_swahili() -> str:
    res = "END Usajili wako umekamilika.\n Utapokea ujumbe wa uthibitisho hivi karibuni!!"
    return res

def help() -> str:
    res = "END For more help on how to use USSD, please follow these steps:\n"
    res += "1. Dial *384*5307# on your phone.\n"
    res += "2. Select the language you want to use.\n"
    res += "3. Follow the instructions on the menu to register.\n"
    res += "For more help, contact 0712345678"
    
    return res
def help_swahili() -> str:
    res = "END Kwa msaada zaidi kuhusu jinsi ya kutumia USSD, tafadhali fuata hatua hizi:\n"
    res += "1. Piga *384*5307# kwenye simu yako.\n"
    res += "2. Chagua lugha unayotaka kutumia.\n"
    res += "3. Fuata maagizo kwenye menyu ili ujiandikishe.\n"
    res += "Kwa msaada zaidi wasiliana na 0712345678"
    
    return res

def get_weather_updates(location) -> str:
    
    subcounty = SubCounty.objects.get(sub_county=location)
    county = subcounty.city
    try:
        updates = Weather.objects.get(city=county)
    except Weather.DoesNotExist:
        return "END Can't get weather updates"
    res = f"END Weather updates for {county}\n"
    res += f"Temperature: {updates.temperature}  °C\n"
    res += f"Description: {updates.description}\n"
    res += f"Humidity: {updates.humidity}\n"
    res += f"Min Temp: {updates.min_temp}  °C\n"
    res += f"Max Temp: {updates.max_temp}  °C\n"
    res += f"Pressure: {updates.pressure}\n"     
    return res

def get_weather_update_swahili(location) -> str:
    subcounty = SubCounty.objects.get(sub_county=location)
    county = subcounty.city
    
    try:
        updates = Weather.objects.get(city=county)
    except Weather.DoesNotExist:
        return "END Taarifa za hali ya hewa hazipatikani"
    res = f"END Taarifa za hali ya hewa {county}\n"
    res += f"Joto: {updates.temperature}  °C\n"
    res += f"Maelezo: {updates.description}\n"
    res += f"Unyevu: {updates.humidity}\n"
    res += f"Joto la chini: {updates.min_temp}  °C\n"
    res += f"Joto la juu: {updates.max_temp}  °C\n"
    res += f"Shinikizo: {updates.pressure}\n"
    return res

@api_view(["POST"])
def mpesa_callback(request):
    
    
    return Response(status=status.HTTP_200_OK)


@api_view(["POST"])
def stk_push(request):
    phone = request.data.get("phone")
    if phone:
        push_stk(phone)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Phone number is required"})
        
    

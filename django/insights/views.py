from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Farm, Activity
from .serializers import FarmSerializer, ActivitySerializer


class FarmViewSet(ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        queryset = Farm.objects.filter(user__id=user.id)
        print("User: ", user.id)
        queryset = Farm.objects.filter(user=user)
        serializer = FarmSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            user = request.user
            if user.is_anonymous:

                return Response(
                    {"error": "Authentication credentials were not provided."},
                    status=status.HTTP_403_FORBIDDEN,
                )

            data = request.data
            data["user"] = user.id
            serializer = FarmSerializer(data=data)
            if serializer.is_valid():
                serializer.save(user=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"message": f"error: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@api_view(["GET"])
def get_farm(request, id):
    try:
        farm = Farm.objects.get(id=id)
        serializer = FarmSerializer(farm)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Farm.DoesNotExist:
        return Response({"error": "Farm not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(
            {"message": "something went wrong", "error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


class ActivityViewset(ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        queryset = Activity.objects.filter(farm__user__id=user.id)
        serializer = ActivitySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            user = request.user
            if user.is_anonymous:

                return Response(
                    {"error": "Authentication credentials were not provided."},
                    status=status.HTTP_403_FORBIDDEN,
                )

            data = request.data
            farm = Farm.objects.get(id=data["farm"])
            if farm.user.id != user.id:
                return Response(
                    {"error": "You are not authorized to perform this action."},
                    status=status.HTTP_403_FORBIDDEN,
                )
            serializer = ActivitySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"message": "something went wrong", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

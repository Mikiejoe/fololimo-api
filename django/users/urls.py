from django.urls import path
from . import views


urlpatterns = [
    path("", views.test, name="test"),
    path("details/",views.get_details,name="get-details"),
]

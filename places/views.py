from django.shortcuts import render
from .serializers import PlaceSerializer
from .models import Place
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import * 
from django.db.models import Q
from .models import *
from PlacesAPI.GM import GenericMethodsMixin
from rest_framework.viewsets import ModelViewSet

def index(request):
    return  render(request, 'places.html')


class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PlaceSerachAPI(APIView) :
    def get(self, request, *args, **kwargs):
        try : 
            search_param = request.GET.get('search')
            if search_param == None :
                all_data =  all_data = Place.objects.all()
                serializer = PlaceSerializer(all_data, many=True)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
           
            q_objects = Q()
            q_objects |= Q(name__icontains=search_param)
            q_objects |= Q(description__icontains=search_param)
            all_data = Place.objects.filter(q_objects)
            serializer = PlaceSerializer(all_data, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except :
            return Response({"error": False,"message": "something went wrong" }, status=status.HTTP_400_BAD_REQUEST)

# class PlaceSearchView(APIView):
#     def get(self, request, format=None):
#         query = request.GET.get("q")
#         if not query:
#             return Response({"places": []})
#         places = Place.objects.filter(
#             full_text__search=query
#         ).order_by("-full_text__score")
#         return Response({"places": list(places)})
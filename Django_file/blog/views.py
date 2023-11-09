from django.shortcuts import render
from rest_framework import viewsets
from .serializers import postTableSerializer,listSerializer,personSerializer,actorSerializer,filmnameSerializer,filmphotoSerializer,TVtableSerializer,RegisterformSerializer
from .models import postTable,List,Person,Actor,Filmname,Filmphoto,TVtable,Registerform

class postTableview(viewsets.ModelViewSet):
  serializer_class=postTableSerializer
  queryset = postTable.objects.all()

class listview(viewsets.ModelViewSet):
  serializer_class=listSerializer
  queryset = List.objects.all()

class personview(viewsets.ModelViewSet):
  serializer_class=personSerializer
  queryset=Person.objects.all()

class actorview(viewsets.ModelViewSet):
  serializer_class=actorSerializer
  queryset=Actor.objects.all()

class filmnameview(viewsets.ModelViewSet):
  serializer_class=filmnameSerializer
  queryset=Filmname.objects.all()

class filmphotoview(viewsets.ModelViewSet):
  serializer_class=filmphotoSerializer
  queryset=Filmphoto.objects.all()

class tvtableview(viewsets.ModelViewSet):
  serializer_class=TVtableSerializer
  queryset=TVtable.objects.all()

class registerformview(viewsets.ModelViewSet):
  serializer_class=RegisterformSerializer
  queryset=Registerform.objects.all()
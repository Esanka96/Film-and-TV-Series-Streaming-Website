from rest_framework import serializers
from .models import postTable,List,Person,Actor,Filmname,Filmphoto,TVtable,Registerform

class listSerializer(serializers.ModelSerializer):
  class Meta:
    model = List
    fields = "__all__"

class personSerializer(serializers.ModelSerializer):
  class Meta:
    model=Person
    fields="__all__"

class actorSerializer(serializers.ModelSerializer):
  class Meta:
    model=Actor
    fields="__all__"

class filmnameSerializer(serializers.ModelSerializer):
  class Meta:
    model=Filmname
    fields="__all__"

class filmphotoSerializer(serializers.ModelSerializer):
  class Meta:
    model=Filmphoto
    fields="__all__"

class postTableSerializer(serializers.ModelSerializer):
  filmnames=filmnameSerializer(many=True,read_only=True)
  filmphotos=filmphotoSerializer(many=True,read_only=True)
  item=listSerializer(many=True,read_only=True)
  persons=personSerializer(many=True,read_only=True)
  actros=actorSerializer(many=True,read_only=True)
  class Meta:
    model = postTable
    fields = "__all__"

class TVtableSerializer(serializers.ModelSerializer):
  class Meta:
    model=TVtable
    fields="__all__"

class RegisterformSerializer(serializers.ModelSerializer):
  class Meta:
    model=Registerform
    fields="__all__"


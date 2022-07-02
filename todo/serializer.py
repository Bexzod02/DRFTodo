from importlib.metadata import MetadataPathFinder
from pyexpat import model
from rest_framework import serializers
from .models import Todo

class Todoserializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("__all__")

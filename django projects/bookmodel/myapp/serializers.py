from rest_framework import serializers
from .models import *

class bookserializer(serializers.ModelSerializer):
    class Meta:
        model=booklist
        fields='__all__'
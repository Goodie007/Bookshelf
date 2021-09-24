#import serializers from rest_framework
from rest_framework import serializers
#import models
from .models import Books

class Books(serializers.HyperLinkedModelSerializer):
    #input fields
    class Meta:
        model = Books
        fields = ('Name', 'Author', 'Genre', 'Year', 'Description')
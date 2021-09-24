from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Books
from .models import Books

# Create your views here.
class BooksViewSet(viewsets.ModelViewSet):
    #queryset
    queryset = Books.objects.all()

    #specify serializer to be used
    serializer_class = Books

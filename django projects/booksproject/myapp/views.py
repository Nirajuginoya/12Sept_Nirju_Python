
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import Bookerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookerializer

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookerializer
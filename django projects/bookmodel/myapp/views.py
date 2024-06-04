from sqlite3 import SQLITE_AUTH_USER
from django.shortcuts import render
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def getall(request):
    bdata=booklist.objects.all()
    serial=bookserializer(bdata,many=True)
    return Response(data=serial.data)


@api_view(['GET'])
def getbookid(request,id):
    try:
        bookid=booklist.objects.get(id=id)
    except booklist.DoesNotExist:
        return Response()  

    serial=bookserializer(bookid)
    return Response(data=serial.data)  

@api_view(['DELETE'])
def deletebookid(request,id):
    try:
        bookid=booklist.objects.get(id=id)
    except booklist.DoesNotExist:
        return Response()  

    booklist.delete(bookid)
    return Response()


@api_view(['DELETE','GET'])
def deletebookid(request,id):
    bookid=''
    if request.method=='GET':
      try:
        bookid=booklist.objects.get(id=id)
      except booklist.DoesNotExist:
        return Response()  
      serial=bookserializer(bookid)
      return Response(data=serial.data)
    if request.method=='DELETE':
       booklist.delete(bookid)
       return Response()
    

@api_view(['post'])    
def savebdata(request):
    if request.method=='POST':
       serial=bookserializer(data=request.data)
       if serial.is_valid():
          serial.save()
          return Response()
       else:
          return Response()
    else:
       return Response ()  



@api_view(['PUT'])
def updatebdata(request,id):
   try:
      bookid=booklist.objects.get(id=id)
   except   booklist.DoesNotExist:
    if request.method=='GET':
      serial=bookserializer(bookid)
      return Response(data=serial.data)   
    if request.method=='PUT':
      serial=bookserializer(request.data)
      if serial.is_valid():
         serial.save()
         return Response()
      else:
         return Response()
    else:
      return Response()
   else:
    return Response()

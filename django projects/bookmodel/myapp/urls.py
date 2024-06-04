from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.getall),
    path('getbookid/<int:id>',views.getbookid),
    path('deletebookid/<int:id>',views.deletebookid),
    path('savebdata/',views.savebdata),
    path('updatebdata/',views.updatebdata),
]
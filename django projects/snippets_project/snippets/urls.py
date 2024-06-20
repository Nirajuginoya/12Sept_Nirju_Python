from django.urls import path
from . import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/<int:snippet_pk>/comments/', views.comment_list),
    path('comments/<int:pk>/', views.comment_detail),
]
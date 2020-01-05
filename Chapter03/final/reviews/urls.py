from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.BooksList.as_view()),
    path('book/<int:pk>/', views.BookDetail.as_view())
]

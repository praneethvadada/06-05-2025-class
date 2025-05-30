# myapp/urls.py
from django.urls import path
from .views import BookList, BookDetail

urlpatterns = [
    path('books/', BookList.as_view()),
    path('books/<str:pk>/', BookDetail.as_view()),
]

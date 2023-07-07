# books/urls.py
from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView,CustomPagination
from . import views

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
    path('myapi/',views.my_api_view, name='myapi'),
]   


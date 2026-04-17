from django.urls import path
from .views import  BookUpdateDestroyView, BookListCreateView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='books'),
    path('books/<int:pk>/', BookUpdateDestroyView.as_view(), name="update"),
    ]
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from .serializers import BookSerializer, CategorySerializer, CommentSerializer, CategorySerializerForDetail
from .models import Book, Category, Comment


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all().select_related('category').only(
        'id', 'name', 'year', 'price', 'category_id').order_by('id')
    serializer_class = BookSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter]
    # filterset_fields = {
    #     'price': ['gt','gte', 'lt', 'lte']
    # }
    # search_fields = ['name', 'price', 'year']


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all().prefetch_related('books')
    serializer_class = CategorySerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = {'name'}
    # ordering_filters = ['name']
    # search_fields = ['name']

    def get_serializer_class(self):
        if self.kwargs.get('pk'):
            return CategorySerializerForDetail
        else:
            return CategorySerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = {'text'}
    search_fields = ['text']
    ordering_filters = ['text']
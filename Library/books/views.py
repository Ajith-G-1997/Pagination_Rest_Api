from rest_framework import generics
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from .pagination import CustomPagination
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(['GET'])
def my_api_view(request):
    paginator = PageNumberPagination()
    queryset = Book.objects.all()
    paginated_queryset = paginator.paginate_queryset(queryset, request)
    serializer = BookSerializer(paginated_queryset, many=True)
    return paginator.get_paginated_response(serializer.data)




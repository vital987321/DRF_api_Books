from rest_framework import viewsets
from myapp.models import Author, Book
from myapp.api.serializers import AuthorSerializer, BookSerializer, AuthorWithBooksSerializer, AuthorWithBooksNameSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class AuthorViewSet(viewsets.ModelViewSet):
    
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

    def get_queryset(self):
        queryset=super().get_queryset()
        name_search=self.request.query_params.get('name-search')
        if name_search:
            queryset=queryset.filter(book__name__contains=name_search)
        return queryset

    @action(methods=['get'], detail=True)
    def showbooks(self, request, pk=None):
        '''Eg:  http://127.0.0.1:8000/author/1/showbooks/   '''
        
        author=super().get_object()
        serializer = AuthorWithBooksSerializer(author)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def allauthors(self, request):
        '''  http://127.0.0.1:8000/author/allauthors/   '''
        
        queryset = super().get_queryset()
        serializer = AuthorWithBooksNameSerializer(queryset, many=True)
        return Response(serializer.data)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        # print('User:',self.request.user)
        serializer.save(name=serializer.validated_data['name']+'!')


    def get_queryset(self):
        queryset=super().get_queryset()
        age=self.request.query_params.get('age')
        if age:
            queryset=queryset.filter(author__age__gte=age)
        return queryset
    

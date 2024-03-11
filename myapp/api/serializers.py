from rest_framework import serializers
from myapp.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorWithBooksSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)  # source='book' - not required if var name is 'book'

    class Meta:
        model = Author
        fields = ['id', 'name', 'age', 'book']


class AuthorWithBooksNameSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name')  

    class Meta:
        model = Author
        fields = ['id', 'name', 'age', 'book']

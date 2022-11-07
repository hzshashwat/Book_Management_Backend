from rest_framework import serializers
from catalog.models import Book

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UpdateBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        name = serializers.CharField(required = False)
        isbn_no = serializers.CharField(required = False)
        author_name = serializers.CharField(required = False)
        genre = serializers.CharField(required = False)
        inventory = serializers.IntegerField(required = False)
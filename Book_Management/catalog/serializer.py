from rest_framework import serializers
from catalog.models import Book

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class ChangeRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'author_name', 'genre', 'inventory']

class UpdateRecordSerializers(serializers.ModelSerializer):
    name = serializers.CharField(required=False, max_length=100, allow_blank=True)
    author_name = serializers.CharField(required=False, max_length=100, allow_blank=True)
    genre = serializers.CharField(required=False, max_length=100, allow_blank=True)
    inventory = serializers.IntegerField(required=False)
    class Meta:
        model = Book
        fields = ['name', 'author_name', 'genre', 'inventory']

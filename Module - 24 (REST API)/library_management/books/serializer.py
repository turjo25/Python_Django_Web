from rest_framework import serializers
from .models import Author,Book


#api te kono form provide korte parbo na
#class meta er moddhe shbkicu e form er moto e
class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True,read_only = True)
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
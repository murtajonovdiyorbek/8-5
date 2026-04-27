from rest_framework import serializers
from .models import Book, Category, Comment


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('category','name','year','price')
        read_only_fields = ('id',)


    def validate_name(self,value):
        if not value.istitle():
            raise serializers.ValidationError("nomi bosh harfi kattada bolishi kerak")

        if not value.isalpha():
            raise serializers.ValidationError("nomi faqat harflardan tashkil topgan bolishi kerak")

        return value

    def validate_year(self,value):
        if not value:
            raise serializers.ValidationError("Yil faqata sondan iborat bolishi kerak")

        return value





class CategorySerializer(serializers.ModelSerializer):
    # books = serializers.StringRelatedField(many=True)
    # books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # books = serializers.HyperlinkedRelatedField(many=True, read_only=True)
    # books = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    # url = serializers.HyperlinkedIdentityField(view_name='category_detail')

    books = BookSerializer(many=True)



    class Meta:
        model = Category
        fields = ('name',)
        read_only_fields = ('id',)

    def validate_name(self,value):
        if not value.istitle():
            raise serializers.ValidationError("Ismni bosh harfi katta bilan yozilishi kerak")

        if not value.isalpha():
            raise serializers.ValidationError("Ism faqat harflardan tashkil topgan bolishi kerak")

        return value



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id',)
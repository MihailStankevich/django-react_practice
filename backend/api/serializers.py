from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note
#чтобы получая данные в формате json конвертировать их и наоборот
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}} #we will not return the password when we give info about the user

    def create(self, validated_data): #it will look on a data/ model we are passing anf if its valid it will be stored in validated_data
        user = User.objects.create_user(**validated_data)
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'author']
        extra_kwargs = {'author': {'read_only': True}} #we dont want to write who the author is, we will do it automatically

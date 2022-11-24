from rest_framework import serializers
from .models import Movie, Actor, Director, Genre, Certification, OTT, Keyword

class MovieSerializer(serializers.ModelSerializer):

    class ActorSerializer(serializers.ModelSerializer):

        class Meta:
            model = Actor
            fields = ('name','profile_path',)
        
    actors = ActorSerializer(many=True, read_only=True)

    class DirectorSerializer(serializers.ModelSerializer):

        class Meta:
            model = Director
            fields = ('name',)
        
    directors = DirectorSerializer(many=True, read_only=True)

    class GenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ('name',)
        
    genres = GenreSerializer(many=True, read_only=True)
    
    class CertificationSerializer(serializers.ModelSerializer):

        class Meta:

            model = Certification
            fields = ('name',)

    certifications = CertificationSerializer(many=True, read_only=True)

    class OTTSerializer(serializers.ModelSerializer):

        class Meta:
            model = OTT
            fields = ('name',)
        
    otts = OTTSerializer(many=True, read_only=True)
   
    class Meta:
        model = Movie
        exclude = ('original_title',)

class MovieMainListSerializer(serializers.ModelSerializer):

    class KeywordSerializer(serializers.ModelSerializer):

        class Meta:
            model = Keyword
            fields = ('id', 'name',)
        
    keywords = KeywordSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = ('id', 'poster_path', 'title', 'video', 'keywords',)



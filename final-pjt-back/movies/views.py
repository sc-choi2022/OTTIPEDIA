from django.shortcuts import get_object_or_404
from movies.models import Movie
from movies.serializers import MovieMainListSerializer, MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random

@api_view(['GET'])
def index(request):
    keyword_list = ['2343', '9840', '180547', '18035', '12565','4344']
    keyword = random.choice(keyword_list)
    movies = Movie.objects.filter(keywords=keyword).order_by('?')[:10]    
    serializer = MovieMainListSerializer(movies,many=True)  
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def recommend_otts(request, ott_id):
    movies = Movie.objects.filter(otts=str(ott_id)).order_by('?')[:5]    
    serializer = MovieMainListSerializer(movies,many=True)  
    return Response(serializer.data)


@api_view(['GET'])
def recommend_directors(request, director_id):
    movies = Movie.objects.filter(directors=str(director_id)).order_by('?')[:5]  
    serializer = MovieMainListSerializer(movies,many=True)  
    return Response(serializer.data)


@api_view(['GET'])
def recommend_keywords(request, keyword_id):
    movies = Movie.objects.filter(keywords=str(keyword_id)).order_by('?')[:5]  
    serializer = MovieMainListSerializer(movies,many=True)  
    return Response(serializer.data)
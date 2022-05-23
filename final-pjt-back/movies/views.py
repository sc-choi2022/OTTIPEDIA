from django.shortcuts import get_object_or_404
from movies.models import Movie
import random

from rest_framework.decorators import api_view
from rest_framework.response import Response

from movies.serializers import MovieMainListSerializer, MovieSerializer

# Create your views here.
@api_view(['GET'])
def index(request):
    keyword_list = ['2343', '9840', '180547', '18035', '12565','4344']
    keyword = random.choice(keyword_list)
    movies = Movie.objects.filter(keywords=keyword).order_by('?')[:10]    
    serializer = MovieMainListSerializer(movies,many=True)  
    return Response(serializer.data)
    # random으로 뽑힌 keyword id 값 넣어주는거 고민해보기


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
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
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movies.models import DoubanMovie
from movies.serializers import MovieSerializer


@api_view(['GET', 'POST'])
def movie_list(request, format=None):
    """
    List all movies, or create a new movie.
    """
    if request.method == 'GET':
        movies = DoubanMovie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk, format=None):
    """
    Retrieve, update or delete a movie.
    """
    try:
        movie = DoubanMovie.objects.get(pk=pk)
    except DoubanMovie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

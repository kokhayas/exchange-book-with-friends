# from django.shortcuts import render
# from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (Author, AuthorBook, Book, BookGenre, Category,
                     ExchangeRequest, Friendship, Genre, Room, University,
                     User, UserBook, UserCategory, UserGenre, UserInfo,
                     UserRoomMessage, UserRoomParticipant)
from .serializers import (AuthorBookSerializer, AuthorSerializer,
                          BookGenreSerializer, BookSerializer,
                          CategorySerializer, ExchangeRequestSerializer,
                          FriendshipSerializer, GenreSerializer,
                          RoomSerializer, UniversitySerializer,
                          UserBookSerializer, UserCategorySerializer,
                          UserGenreSerializer, UserInfoSerializer,
                          UserRoomMessageSerializer,
                          UserRoomParticipantSerializer, UserSerializer)


@api_view(["GET", "POST"])
def getUsers(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



class AuthorBookViewSet(viewsets.ModelViewSet):
    queryset = AuthorBook.objects.all()
    serializer_class = AuthorBookSerializer


class BookGenreViewSet(viewsets.ModelViewSet):
    queryset = BookGenre.objects.all()
    serializer_class = BookGenreSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


class UserBookViewSet(viewsets.ModelViewSet):
    queryset = UserBook.objects.all()
    serializer_class = UserBookSerializer


class UserCategoryViewSet(viewsets.ModelViewSet):
    queryset = UserCategory.objects.all()
    serializer_class = UserCategorySerializer


class UserGenreViewSet(viewsets.ModelViewSet):
    queryset = UserGenre.objects.all()
    serializer_class = UserGenreSerializer


class UserRoomMessageViewSet(viewsets.ModelViewSet):
    queryset = UserRoomMessage.objects.all()
    serializer_class = UserRoomMessageSerializer


class UserRoomParticipantViewSet(viewsets.ModelViewSet):
    queryset = UserRoomParticipant.objects.all()
    serializer_class = UserRoomParticipantSerializer


class ExchangeRequestViewSet(viewsets.ModelViewSet):
    queryset = ExchangeRequest.objects.all()
    serializer_class = ExchangeRequestSerializer


class FriendshipViewSet(viewsets.ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer


# @api_view(["GET"])
# def getRoutes(request):
#     routes = [
#         {
#             "Endpoint": "/ingredients/",
#             "method": "GET",
#             "url": "http://localhost:8000/api/ingredients",
#         },
#     ]
#     return Response(routes)


# @api_view(["GET", "POST"])
# def getIngredients(request):
#     if request.method == "GET":
#         ingredients = Ingredients.objects.all()
#         serializer = IngredientsSerializer(ingredients, many=True)
#         return Response(serializer.data)
#     if request.method == "POST":
#         data = request.data
#         ingredient = Ingredients.objects.create(body=data["body"])
#         serializer = IngredientsSerializer(ingredient, many=False)
#         return Response(serializer.data)


# @api_view(["GET", "PUT", "DELETE"])
# def getIngredient(request, pk):
#     pass

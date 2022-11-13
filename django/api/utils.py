from rest_framework import status, viewsets
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


def getUserList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


def createUser(request):
    data = request.data
    user = User.objects.create(
        body=data['data']
    )
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


def getUserDetail(request, user_id):
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

def updateUser(request, user_id):
    user = User.objects.get(id=user_id)
    data = request.data
    user.body = data['data']
    user.save()
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

def deleteUser(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return Response("User was deleted")


def getBookList(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

def createBook(request):
    data = request.data
    book = Book.objects.create(
        body=data['data']
    )
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)

def getBookDetail(request, book_id):
    book = Book.objects.get(id=book_id)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)

def updateBook(request, book_id):
    book = Book.objects.get(id=book_id)
    data = request.data
    book.body = data['data']
    book.save()
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)

def deleteBook(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return Response("Book was deleted")


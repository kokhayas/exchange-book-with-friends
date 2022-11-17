from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (
    Author,
    AuthorBook,
    Book,
    BookGenre,
    Category,
    ExchangeRequest,
    Friendship,
    Genre,
    Note,
    Room,
    University,
    User,
    UserBook,
    UserCategory,
    UserGenre,
    UserInfo,
    UserRoomMessage,
    UserRoomParticipant,
)
from .serializers import (
    AuthorBookSerializer,
    AuthorSerializer,
    BookGenreSerializer,
    BookSerializer,
    CategorySerializer,
    ExchangeRequestSerializer,
    FriendshipSerializer,
    GenreSerializer,
    NoteSerializer,
    RoomSerializer,
    UniversitySerializer,
    UserBookSerializer,
    UserCategorySerializer,
    UserGenreSerializer,
    UserInfoSerializer,
    UserRoomMessageSerializer,
    UserRoomParticipantSerializer,
    UserSerializer,
)


def getUserList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


def createUser(request):
    data = request.data
    user = User.objects.create(body=data["data"])
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


def getUserDetail(request, user_id):
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


def updateUser(request, user_id):
    user = User.objects.get(id=user_id)
    data = request.data
    user.body = data["data"]
    user.save()
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


def deleteUser(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return Response("User was deleted")


def getNoteList(request):
    # user = request.user
    # notes = user.note_set.all()
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


def createNote(request):
    data = request.data
    note = Note.objects.create(body=data["data"])
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


def getNoteDetail(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


def updateNote(request, pk):
    note = Note.objects.get(id=pk)
    data = request.data
    note.body = data["data"]
    note.save()
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note was deleted")


def getBookList(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


def createBook(request):
    data = request.data
    book = Book.objects.create(body=data["data"])
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)


def getBookDetail(request, book_id):
    book = Book.objects.get(id=book_id)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)


def updateBook(request, book_id):
    book = Book.objects.get(id=book_id)
    data = request.data
    book.body = data["data"]
    book.save()
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)


def deleteBook(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return Response("Book was deleted")

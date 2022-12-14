# from django.shortcuts import render
# from rest_framework import viewsets
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

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
from .utils import (
    createBook,
    createNote,
    createUser,
    deleteBook,
    deleteNote,
    deleteUser,
    getBookDetail,
    getBookList,
    getNoteDetail,
    getNoteList,
    getUserDetail,
    getUserList,
    updateBook,
    updateNote,
    updateUser,
)

# @api_view(["GET"])
# def getRoutes(request):
#     routes = [
#         "/api/token/",
#         "/api/token/refresh/",
#     ]
#     return Response(routes)


# /api/users/ GET
# /api/users/ POST

# /api/users/<id>/ GET
# /api/user/<id>/ PUT
# /api/user/<id>/ DELETE


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET", "POST"])
def getUsers(request):
    if request.method == "GET":
        return getUserList(request)
    elif request.method == "POST":
        return createUser(request)


@api_view(["GET", "PUT", "DELETE"])
def getUser(request, pk):
    if request.method == "GET":
        return getUserDetail(request, pk)

    elif request.method == "PUT":
        return updateUser(request, pk)

    elif request.method == "DELETE":
        return deleteUser(request, pk)


# /api/v1/books/ GET
# /api/v1/books/ POST

# /api/v1/book/<id>/ GET
# /api/v1/book/<id>/ PUT
# /api/v1/book/<id>/ DELETE


# @api_view(["GET", "POST"])
# @permission_classes([IsAuthenticated])
# def getNotes(request):
#     if request.method == "GET":
#         return getNoteList(request)
#     elif request.method == "POST":
#         return createNote(request)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    notes = user.note_set.all()
    # notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def getNote(request, pk):
    if request.method == "GET":
        return getNoteDetail(request, pk)

    elif request.method == "PUT":
        return updateNote(request, pk)

    elif request.method == "DELETE":
        return deleteNote(request, pk)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def getBooks(request):
    # user = request.user
    # books = user.book_set.all()
    if request.method == "GET":
        return getBookList(request)
    elif request.method == "POST":
        return createBook(request)


@api_view(["GET", "PUT", "DELETE"])
def getBook(request, pk):
    if request.method == "GET":
        return getBookDetail(request, pk)

    elif request.method == "PUT":
        return updateBook(request, pk)

    elif request.method == "DELETE":
        return deleteBook(request, pk)


# this is the intermediate table between User and Book

# class UserBook(models.Model):
#     pk = models.ForeignKey(User, on_delete=models.CASCADE)
#     pk = models.ForeignKey(Book, null=True, blank=True, on_delete=models.CASCADE)
#     my_title = models.CharField(max_length=128, null=False, default="", blank=True)
#     my_description = models.TextField(null=False, default="", blank=True)
#     my_info_url = models.URLField(max_length=2048, null=False, default="", blank=True)
#     my_image_url = models.URLField(max_length=2048, null=False, default="", blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_sharable = models.BooleanField(default=True)
#     is_being_shared = models.BooleanField(default=False)
#     requested_number = models.IntegerField(default=0)


# api that gets name of book of a user
@api_view(["GET", "POST"])
def getUserBooks(request):
    if request.method == "GET":
        userbooks = UserBook.objects.all()
        serializer = UserBookSerializer(userbooks, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = UserBookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def getUserBook(request, pk):
    try:
        user_book = UserBook.objects.get(id=pk)
    except UserBook.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserBookSerializer(user_book)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = UserBookSerializer(user_book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        user_book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


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

# from django.urls import path
from rest_framework import routers

from django.urls import include, path

from . import views

# urlpatterns = [
#     path("", views.getRoutes),
#     path("ingredients", views.getIngredients),
#     path("ingredient/<str:pk>/", views.getIngredient),
# ]

# Author, Book, Genre, Room, University, User, UserInfo

# from .serializers import (
#     AuthorBookSerializer,
#     AuthorSerializer,
#     BookGenreSerializer,
#     BookSerializer,
#     CategorySerializer,
#     ExchangeRequestSerializer,
#     FriendshipSerializer,
#     GenreSerializer,
#     RoomSerializer,
#     UniversitySerializer,
#     UserBookSerializer,
#     UserCategorySerializer,
#     UserGenreSerializer,
#     UserInfoSerializer,
#     UserRoomMessageSerializer,
#     UserRoomParticipantSerializer,
#     UserSerializer,
# )

router = routers.DefaultRouter()

router.register("authors", views.AuthorViewSet)
router.register("books", views.BookViewSet)
router.register("genres", views.GenreViewSet)
router.register("rooms", views.RoomViewSet)
router.register("universities", views.UniversityViewSet)
router.register("users", views.UserViewSet)
router.register("userinfos", views.UserInfoViewSet)
router.register("authorbooks", views.AuthorBookViewSet)
router.register("bookgenres", views.BookGenreViewSet)
router.register("categories", views.CategoryViewSet)
router.register("usercategories", views.UserCategoryViewSet)
router.register("usergenres", views.UserGenreViewSet)
router.register("userroommessages", views.UserRoomMessageViewSet)
router.register("userroomparticipants", views.UserRoomParticipantViewSet)
router.register("exchangerequests", views.ExchangeRequestViewSet)
router.register("friendships", views.FriendshipViewSet)
router.register("userbook", views.UserBookViewSet)


# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("api/token/", views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("viewset", include(router.urls)),
    path("users", views.getUsers, name="users"),
    path("user/<str:user_id>/", views.getUser, name="user"),
    path("books", views.getBooks, name="books"),
    path("book/<str:book_id>/", views.getBook, name="book"),
    path("userbooks", views.getUserBooks, name="userbooks"),
    path("userbook/<str:user_book_id>/", views.getUserBook, name="userbook"),
]

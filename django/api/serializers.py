from rest_framework import serializers

from django.contrib.auth.hashers import make_password  # 追加

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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate_password(self, value: str) -> str:
        return make_password(value)


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class UserCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCategory
        fields = "__all__"


class AuthorBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorBook
        fields = "__all__"


class UserRoomParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoomParticipant
        fields = "__all__"


class UserRoomMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoomMessage
        fields = "__all__"


class UserBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBook
        fields = "__all__"


class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = "__all__"


class ExchangeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRequest
        fields = "__all__"


class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        fields = "__all__"


class UserGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGenre
        fields = "__all__"

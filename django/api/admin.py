from django.contrib import admin

# Register your models here.
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
    UserBook,
    UserCategory,
    UserGenre,
    UserInfo,
    UserRoomMessage,
    UserRoomParticipant,
)

admin.site.register(Note)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(AuthorBook)
admin.site.register(BookGenre)
admin.site.register(Category)
admin.site.register(ExchangeRequest)
admin.site.register(Friendship)
admin.site.register(Genre)
admin.site.register(Room)
admin.site.register(University)
admin.site.register(UserBook)
admin.site.register(UserCategory)
admin.site.register(UserGenre)
admin.site.register(UserInfo)
admin.site.register(UserRoomMessage)
admin.site.register(UserRoomParticipant)

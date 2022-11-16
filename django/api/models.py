from django.contrib.auth import get_user_model
from django.db import models

# language is in order of population

LANGUAGE_CHOICES = (
    ("en", "english"),
    ("sp", "spanish"),
    ("ch", "chinese"),
    ("gm", "german"),
    ("jp", "japanese"),
    ("kr", "korean"),
    ("hb", "hebrew"),
)

User = get_user_model()


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()


class Book(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=False, default="", blank=True)
    info_url = models.URLField(max_length=2048, null=False, default="", blank=True)
    image_url = models.URLField(max_length=2048, null=False, default="", blank=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=128)
    english_name = models.CharField(max_length=128, default="")
    description = models.TextField(null=False, default="", blank=True)
    info_url = models.URLField(max_length=2048, null=False, default="", blank=True)
    image_url = models.URLField(max_length=2048, null=False, default="", blank=True)

    def __str__(self):
        return self.name


class University(models.Model):
    university = models.CharField(max_length=128)
    student_mail_address_endpoint = models.CharField(
        max_length=128, null=False, default="", blank=True
    )
    alumni_mail_address_endpoint = models.CharField(
        max_length=128, null=False, default="", blank=True
    )

    def __str__(self):
        return self.university


class Genre(models.Model):
    genre = models.CharField(max_length=128)
    description = models.TextField(null=False, default="", blank=True)
    image_url = models.URLField(max_length=2048, null=False, default="", blank=True)

    def __str__(self):
        return self.genre


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=False, default="", blank=True)
    image_url = models.URLField(max_length=2048, null=False, default="", blank=True)
    info_url = models.URLField(max_length=2048, null=False, default="", blank=True)

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pen_name = models.CharField(max_length=128, null=False, default="", blank=True)
    gender_code = models.CharField(max_length=1, null=False, default="", blank=True)
    age = models.PositiveIntegerField(blank=True, null=False, default=0)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default="ja")
    university_email = models.EmailField(
        max_length=128, null=False, default="", blank=True
    )
    university_code = models.ForeignKey(
        University, on_delete=models.CASCADE, blank=True, null=True
    )
    phone_number = models.CharField(max_length=128, null=False, default="", blank=True)
    second_email = models.EmailField(max_length=128, null=False, default="", blank=True)
    exchanged_number = models.IntegerField(default=0)
    being_blocked_number = models.IntegerField(default=0)
    is_banned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=256, blank=True, null=False, default="")
    birth_date = models.DateField(null=True, blank=True)
    share_url = models.URLField(max_length=2048, null=False, default="", blank=True)

    def __str__(self):
        return self.user.username


class Room(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_pair = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class UserCategory(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.username + " " + self.category_id.name


class AuthorBook(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.author_id.name + " " + self.book_id.title


class UserRoomParticipant(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_user_active = models.BooleanField(default=True)
    is_room_muted = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id.username + " " + self.room_id.name


class UserRoomMessage(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_modified = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id.username + " " + self.room_id.name


class UserBook(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, null=True, blank=True, on_delete=models.CASCADE)
    my_title = models.CharField(max_length=128, null=False, default="", blank=True)
    my_description = models.TextField(null=False, default="", blank=True)
    my_info_url = models.URLField(max_length=2048, null=False, default="", blank=True)
    my_image_url = models.URLField(max_length=2048, null=False, default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_sharable = models.BooleanField(default=True)
    is_being_shared = models.BooleanField(default=False)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user_id.username + " " + self.book_id.title


class Friendship(models.Model):
    # pending_first_second, pending_second_first, friends, block_first_second, block_second_first, block_both
    INITIALIZED = 0
    PENDING_FIRST_SECOND = 1
    PENDING_SECOND_FIRST = 2
    FRIENDS = 3
    BLOCK_FIRST_SECOND = 4
    BLOCK_SECOND_FIRST = 5
    BLOCK_BOTH = 6
    Status = (
        (INITIALIZED, "initialized"),
        (PENDING_FIRST_SECOND, "pending_first_second"),
        (PENDING_SECOND_FIRST, "pending_second_first"),
        (FRIENDS, "friends"),
        (BLOCK_FIRST_SECOND, "block_first_second"),
        (BLOCK_SECOND_FIRST, "block_second_first"),
        (BLOCK_BOTH, "block_both"),
    )
    requester_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="friendship_requester_id"
    )
    addressee_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="friendship_addressee_id"
    )
    status_id = models.IntegerField(choices=Status, default=INITIALIZED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            self.requester_id.username
            + " "
            + self.addressee_id.username
            + " "
            + self.status_id
        )


class ExchangeRequest(models.Model):
    # pending, accepted, rejected, canceled
    PENDING = 0
    ACCEPTED = 1
    REJECTED = 2
    CANCELED = 3
    Status = (
        (PENDING, "pending"),
        (ACCEPTED, "accepted"),
        (REJECTED, "rejected"),
        (CANCELED, "canceled"),
    )
    requester_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="exchange_requester_id"
    )
    addressee_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="exchange_addressee_id"
    )
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    status_id = models.IntegerField(choices=Status, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            self.requester_id.username
            + " "
            + self.addressee_id.username
            + " "
            + self.book_id.title
            + " "
            + self.status_id
        )


class BookGenre(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_id.title + " " + self.genre_id.name


class UserGenre(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.username + " " + self.genre_id.name


# class Ingredient(models.Model):
#     name = models.CharField(null=True, blank=True, max_length=128)
#     info_url = models.URLField(null=True, blank=True, max_length=128)
#     shelf_life_days = models.PositiveIntegerField(null=True, blank=True, default=365)
#     owners = models.ManyToManyField(
#         User, through="UserIngredient", related_name="ingredients"
#     )

#     def __str__(self):
#         return self.name


# class Recipe(models.Model):
#     title = models.CharField(unique=True, max_length=128)
#     recipe_url = models.URLField(null=True, blank=True, max_length=128)
#     image_url = models.URLField(null=True, blank=True, max_length=128)
#     cook_minute = models.FloatField(
#         validators=[MinValueValidator(0.0)], null=True, blank=True
#     )
#     num_servings = models.PositiveIntegerField(null=True, blank=True)
#     language = models.CharField(default="en", max_length=2, choices=LANGUAGE_CHOICES)
#     ingredients = models.ManyToManyField(
#         Ingredient, through="RecipeIngredient", related_name="recipes"
#     )
#     users_who_cooked = models.ManyToManyField(
#         User, through="UserRecipeHistory", related_name="cooked_recipes"
#     )
#     users_who_liked = models.ManyToManyField(
#         User, through="UserRecipeFavorite", related_name="liked_recipes"
#     )

#     def __str__(self):
#         return self.title


# class Tag(models.Model):
#     name = models.CharField(max_length=128)
#     description = models.CharField(null=True, blank=True, max_length=128)
#     tag_url = models.URLField(null=True, blank=True, max_length=128)
#     image_url = models.URLField(null=True, blank=True, max_length=128)
#     language = models.CharField(default="en", max_length=2, choices=LANGUAGE_CHOICES)
#     recipes = models.ManyToManyField(Recipe, through="RecipeTag", related_name="tags")

#     def __str__(self):
#         return self.name


# class UserIngredient(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
#     consumed = models.BooleanField(default=False)
#     created_date = models.DateTimeField(auto_now_add=True)
#     purchase_date = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return f"user: {str(self.user)}, ingredient: {str(self.ingredient)}"


# class RecipeIngredient(models.Model):
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
#     ingredient_quantity = models.CharField(default="1", max_length=128)

#     def __str__(self):
#         return f"recipe: {str(self.recipe)}, ingredient: {str(self.ingredient)}"


# class RecipeTag(models.Model):
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"recipe: {str(self.recipe)}, tag: {str(self.tag)}"


# class RecipeNutrition(models.Model):
#     recipe = models.OneToOneField(
#         Recipe, on_delete=models.CASCADE, primary_key=True, related_name="nutrition"
#     )
#     calories_kcal_per_serving = models.FloatField(
#         validators=[MinValueValidator(0.0)], default=0
#     )
#     fat_gram_per_serving = models.FloatField(
#         validators=[MinValueValidator(0.0)], null=True, blank=True
#     )
#     carbs_gram_per_serving = models.FloatField(
#         validators=[MinValueValidator(0.0)], null=True, blank=True
#     )
#     protein_gram_per_serving = models.FloatField(
#         validators=[MinValueValidator(0.0)], null=True, blank=True
#     )

#     def __str__(self):
#         return ", ".join(
#             [
#                 f"Recipe: {self.recipe.title}",
#                 f"Energy: {self.calories_kcal_per_serving} kCal",
#                 f"Protein: {self.protein_gram_per_serving} g",
#                 f"Fat: {self.fat_gram_per_serving} g",
#                 f"Carb: {self.carbs_gram_per_serving} g",
#             ]
#         )


# class UserRecipeHistory(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     cooked_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"user: {str(self.user)}, recipe: {str(self.recipe)}"


# class UserRecipeFavorite(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     added_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"user: {str(self.user)}, recipe: {str(self.recipe)}"

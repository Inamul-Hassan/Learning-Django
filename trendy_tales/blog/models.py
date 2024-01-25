from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Tag(models.Model):
    tags = models.CharField(max_length=30)

    def __str__(self):
        return self.tags


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Posts(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default="", null=False, db_index=True, unique=True)
    excert = models.CharField(max_length=200)
    content = models.TextField(validators=[MinLengthValidator(10)])
    date_added = models.DateField(auto_now_add=True)
    image_name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

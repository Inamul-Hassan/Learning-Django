from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    # author = models.CharField(max_length=50, blank=True, null=True)
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False,
                            db_index=True)

    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"

    def get_absolute_url(self):
        return reverse("detailed", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

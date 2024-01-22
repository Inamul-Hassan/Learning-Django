from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    author = models.CharField(max_length=50, blank=True, null=True)
    is_bestseller = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"

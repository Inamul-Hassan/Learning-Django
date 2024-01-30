from django.db import models

# Create your models here.


class ReviewModel(models.Model):
    user_name = models.CharField(max_length=100)
    reviews = models.TextField(max_length=200)
    rating = models.IntegerField()

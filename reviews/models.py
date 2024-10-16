from django.db import models

class Review(models.Model):
    text = models.TextField()
    status = models.CharField(max_length=10)
    rating = models.IntegerField()

    def __str__(self):
        return self.text

# Create your models here.

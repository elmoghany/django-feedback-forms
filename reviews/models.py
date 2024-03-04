from django.db import models

# Create your models here.
# models are created for database
class Review(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()
    # owner_comment = models.TextField()
from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, 'Draft'), (1, 'Publish'))
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now = True)
    slug = models.SlugField(max_length = 200, unique = True)
    author = models.ForeignKey(to = User, on_delete = models.CASCADE)
    status = models.IntegerField(choices = STATUS, default = 0)

    # Determines what we see when we print out one of these models
    def __str__(self):
        return self.title
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#one to many relationship. One user can have multiple posts
#one post can have only one user

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.URLField(max_length = 200)
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='album/imageposts', height_field=None, width_field=None, max_length=100)
    def __str__(self):
        return self.title

    # image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    




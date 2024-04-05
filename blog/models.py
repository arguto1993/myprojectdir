from django.conf import settings
from django.db import models
from django.utils import timezone

# Many-to-Many Relationship:
# Let's say we want to create a Tag model where each post can have multiple tags, 
# and each tag can be associated with multiple posts.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_date = models.DateTimeField(default=timezone.now)

    def create_comment(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
    
# User has a One to many relationship with Post
# One user can have multiple post
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        # return f"{self.title} by Author {self.author}"
        return self.title

# Post has a One to many relationship with Comment
# One Post can have multiple comments
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def create_comment(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        # return f"Comment by {self.author} on {self.post.title}"
        return self.text
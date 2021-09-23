from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    follow = models.ManyToManyField(to="self", related_name="followers", symmetrical=False, blank=True)

class Post(models.Model):
    def __str__(self):
        identifier = str(self.user)+": "
        if len(str(self.body))>20:
            identifier += str(self.body)[0:17]+"..."
        else:
            identifier += str(self.body)
        identifier += " - "+str(self.timestamp)
        return identifier
    body = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name="post", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)


class PostLike(models.Model):
    def __str__(self):
        identifier = str(self.user)+"+"
        identifier += "\n"+str(self.post)
        return identifier
    user = models.ForeignKey(User, related_name="post_like", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="like", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "post"], name="unique_post_like"
            )
        ]

from django.db import models

# Create your models here.

class Follow(models.Model):
    follower = models.ForeignKey('users.User', related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey('users.User', related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following') # A user can follow another user only once

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"


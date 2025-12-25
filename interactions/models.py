from django.db import models

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on Post {self.post.id}"

class Like(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user') # A user can like a post only once

    def __str__(self):
        return f"Like by {self.user.username} on Post {self.post.id}"

class Follow(models.Model):
    follower = models.ForeignKey('users.User', related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey('users.User', related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following') # A user can follow another user only once

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"


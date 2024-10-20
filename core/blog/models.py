from django.db import models
from django.conf import settings

# Create your models here.
user = settings.AUTH_USER_MODEL
class category(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title
    
class tag(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title
    

class Post(models.Model):
    author = models.ForeignKey(user , on_delete=models.CASCADE)
    category = models.ManyToManyField(category,null=True, blank=True)
    tag = models.ManyToManyField(tag,null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return str(self.author) + " - " + self.title

class Like(models.Model):
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    author = models.ForeignKey(user, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'author') 

    def __str__(self):
        return str(self.author)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name="replies", on_delete=models.CASCADE)
    
    def __str__(self):
        # if self.parent:
        #     return f'{self.id} - {self.author}'
        return f'{self.id} - {self.post.title}'



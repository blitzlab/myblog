from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)
    date_published = models.DateTimeField(null = True, blank = True)

    def publish(self):
        self.date_published = timezone.now()
        self.save()

    def approve_comment(self):
        return self.comments.filter(approved_comments = True)
    
    def get_absolute_url(self):
        return reverse("blog:post_list", kwargs={"pk": self.pk})
    

    def __str__(self):
        return title

class Comment(models.Model):
    post = models.ForeignKey("blog.Post", related_name = 'comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)
    approved_comments = models.BooleanField(default = False)

    def approve(self):
        self.approved_comments = True
        self.save()

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.text
from django.db import models

# Create your models here.
class Bookmarks(models.Model):
    title = models.CharField(max_length=200, blank=False)
    url = models.URLField(max_length=200, blank=False)
    description = models.TextField()
    image = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

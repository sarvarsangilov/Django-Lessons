from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to="images/")
    creadet_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
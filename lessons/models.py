from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="lessons/", blank=True, null=True)

    def __str__(self):
        return self.title
from django.conf import settings
from django.db import models
from django.utils import timezone



class Post(models.Model):
    auther = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.BooleanField(default=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.

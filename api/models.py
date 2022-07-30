from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

STATUS = (
    ("In Progress","In Progress"),
    ("Completed","Completed"),
)

class Client(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    phone=models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client_posts')
    created_at= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email


class Project(models.Model):
    title=models.CharField(max_length=500)
    description=models.TextField(blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='project_posts')
    slug = models.SlugField(max_length=200, unique=True,unique_for_date='created_at')
    status=models.CharField(max_length=200,choices=STATUS, default="In Progress")
    client=models.ForeignKey(Client, related_name='clients', on_delete= models.CASCADE)
    created_at= models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
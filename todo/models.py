from django.db import models
from django.utils.timezone import now

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=300)
    description = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
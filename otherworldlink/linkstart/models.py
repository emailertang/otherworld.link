from django.db import models

# Create your models here.
class Index(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(null=True)
    def __str__(self):
        return self.title
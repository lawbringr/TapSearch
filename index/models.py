from django.db import models

# Create your models here.
class Document(models.Model):
    name=models.CharField(default="No Name", max_length=50)
    doc=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
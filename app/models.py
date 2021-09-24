from django.db import models

# Create your models here.
class Books (model.Models):
    title = models.CharField(max_length = 200)
    description = models.TextField()

    def__str__(self):
        return self.title
from django.db import models
# Create your models here.
class Contact(models.Model):
    name = models.TextField(null=True)
    email = models.TextField(null=True)
    phone = models.TextField(null=True)
    message = models.TextField(null=True)
    def __str__(self):
        return self.name
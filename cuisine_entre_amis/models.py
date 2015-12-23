from django.db import models


class Contact(models.Model):

  name = models.CharField(max_length=100)
  mail = models.EmailField(max_length=100)
  phone = models.CharField(max_length=100)
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

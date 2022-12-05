"""
Definition of models.
"""

from django.db import models

class Contact(models.Model):
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=10)
    feedback=models.TextField()
    date=models.DateField()

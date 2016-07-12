from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Text(models.Model):
    name = models.CharField(max_length=10)
    head = models.TextField(null=True)
    body = models.TextField(null=True)
    filePaths = models.TextField(null=True)
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

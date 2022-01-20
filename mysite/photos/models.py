from __future__ import unicode_literals

from django.db import models

class Photo(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
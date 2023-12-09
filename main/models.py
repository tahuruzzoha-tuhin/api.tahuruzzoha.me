from django.db import models


class BaseBlogModel(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    slug = models.CharField(max_length=30, null=True, blank=True)
    subtitle = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField()
    created_at = models.DateField(auto_now=True)


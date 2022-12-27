from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField('Project Name', max_length=70, unique=True)
    description = models.TextField('Project Description')
    color = models.CharField('Color', max_length=30)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Created by')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

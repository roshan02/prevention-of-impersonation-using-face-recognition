from __future__ import unicode_literals

from django.db import models

class Day(models.Model):
    name = models.CharField(max_length = 10)
    DSA = models.BooleanField(default=False)
    DLD = models.BooleanField(default=False)
    DSGT = models.BooleanField(default=False)
    SLS = models.BooleanField(default=False)
    ODE = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Todo(models.Model):
    task = models.CharField(max_length = 50)
    last = models.CharField(max_length = 10)

    def __str__(self):
        return self.task

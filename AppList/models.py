# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class Tareas(models.Model):
    
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)


    #metodo para mostrar el titulo en el panel admin
    def __str__(self):
        return self.title
from django.contrib import admin
from django.db import models

class Question(models.Model):
    question_text = models.CharField
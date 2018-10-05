from django.db import models
from django.utils import timezone
from markdown import markdown
from taggit.managers import TaggableManager
from .subjects import *


class Conspect(models.Model):
    title = models.CharField(max_length=100)
    subject = models.IntegerField(choices=SUBJECT_CHOICES, default=0)
    description = models.CharField(max_length=200)
    text = models.TextField()
    tags = TaggableManager()
    raters = models.CharField(max_length=5000)
    average_rating = models.FloatField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    html_field = models.TextField(editable=False)


    def get_subject(self):
        return SUBJECT_CHOICES[self.subject][1]


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title


    def save(self):
        self.html_field = markdown(self.text)
        super(Conspect, self).save()

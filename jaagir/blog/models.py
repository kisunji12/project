from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title           = models.CharField(max_length=100)
    job_description = models.TextField()
    post_date       = models.DateTimeField(default=timezone.now)
    author          = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def snippet(self):
        return self.job_description[:80]+'...'


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})


Qualification_Choices = (('slc', 'SLC'), ('+2', '+2'), ('bachelor', 'Bachelor'))

class ApplicationForm(models.Model):
    full_name       = models.CharField(max_length=200)
    address         = models.CharField(max_length=200)
    age             = models.IntegerField()
    contact         = models.IntegerField()
    qualification   = models.CharField(max_length=100, choices=Qualification_Choices)
    job_post        = models.OneToOneField(Post, on_delete=models.CASCADE)
    applicant       = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.job_post}-{self.full_name}'

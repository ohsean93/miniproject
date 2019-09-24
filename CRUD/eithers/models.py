from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=300)
    issue_a = models.CharField(max_length=300, default='agree')
    issue_b = models.CharField(max_length=300, default='disagree')
    image_a = models.ImageField(default=None)
    image_b = models.ImageField(default=None)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete='CASCADE')
    pick = models.IntegerField(default=0)
    comment = models.CharField(max_length=300)

    class Meta:
        ordering = ['-pk']
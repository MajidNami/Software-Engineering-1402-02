from django.db import models

# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class UserResult(models.Model):
    user = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.score}"

from django.db import models

class Word(models.Model):
    text = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.text

class Game(models.Model):
    target_word = models.CharField(max_length=5)
    guesses = models.JSONField(default=list)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Game - {self.target_word}"

from django.db import models

class Leaderboard(models.Model):
    name = models.CharField(max_length=100)
    attempts = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

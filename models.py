from django.db import models

class Game(models.Model):
    SETUP = 'SE'
    PLAYING = 'PL'
    FINISHED = 'FI'
    STATE_CHOICES = (
        (SETUP, 'Setup'),
        (PLAYING, 'Playing'),
        (FINISHED, 'Finished')
    )
    name = models.CharField(max_length=1000)
    max_players = models.IntField()
    created = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, default=SETUP)

class Player(models.Model):
    name = models.CharField(max_length=1000)
    game = models.ForeignKey("Game")
    ready = models.BooleanField(default=False)

class Message(models.Model):
    data = models.TextField()
    game = models.ForeignKey("Game")
    sender = models.ForeignKey("Player")
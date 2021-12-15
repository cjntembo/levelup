from django.db import models
from levelupapi.models.gameType import GameType
from levelupapi.models.gamer import User


class Game(models.Model):
    name = models.CharField(max_length=55)
    gametype = models.ForeignKey(GameType, on_delete=models.CASCADE, related_name='games')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
from django.db import models
from levelupapi.models.gametype import GameType
from levelupapi.models.gamer import User


class Game(models.Model):
    title = models.CharField(max_length=55)
    maker = models.CharField(max_length=55, null=True)
    gamer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games')
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE, related_name='games')
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()
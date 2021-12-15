from django.db import models

from levelupapi.models.status import Status

class Event(models.Model):
    game = models.ForeignKey("levelupapi.game", on_delete=models.CASCADE, related_name='games')
    eventDate = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='status')
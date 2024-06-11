from django.db import models
from datetime import datetime


class ReceivedMessages(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name_plural = 'Received Messages'

    def __str__(self):
        return f'{self.date:%Y/%m/%d} - {self.email}'


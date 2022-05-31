from django.db import models


class HitCount(models.Model):
    path = models.CharField(max_length=512)
    hits = models.IntegerField(default=1)
    user = models.CharField(max_length=128)

    def __str__(self):
        user = self.user if self.user else 'AnonymousUser'
        return f'{user} : [ {self.path} ]   ({self.hits})'

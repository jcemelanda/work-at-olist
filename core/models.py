from django.db import models


class CallRecord(models.Model):
    type = models.CharField(max_length=5, choices=(('start', 'start'), ('end', 'end')))
    timestamp = models.DateTimeField(auto_now_add=True)
    call_id = models.PositiveIntegerField()
    source = models.CharField(max_length=11)
    destination = models.CharField(max_length=11)
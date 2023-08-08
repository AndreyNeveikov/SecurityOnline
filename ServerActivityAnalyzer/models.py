from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=80, null=True, blank=True)
    url = models.CharField(max_length=80, unique=True, null=False, blank=False)
    description = models.TextField(null=True, blank=True)


class ServerResponse(models.Model):
    response_from = models.ForeignKey(
        to='Server',
        on_delete=models.CASCADE,
        related_name='servers')
    response_code = models.CharField(max_length=3, null=False, blank=False)
    response_payload = models.CharField(max_length=80, null=True, blank=True)
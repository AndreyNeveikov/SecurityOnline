from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=80, null=True, blank=True)
    url = models.CharField(max_length=80, unique=True, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Server (id: {self.id}, name: {self.name}, url: {self.url}), description: {self.description}"


class ServerResponse(models.Model):
    response_from = models.ForeignKey(
        to='Server',
        on_delete=models.CASCADE,
        related_name='servers')
    response_code = models.CharField(max_length=3, null=False, blank=False)
    response_time = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"Server (id: {self.id}, response_from: {self.response_from}, response_code: {self.response_code}), "
                f"response_time: {self.response_time}, created_at: {self.created_at}")

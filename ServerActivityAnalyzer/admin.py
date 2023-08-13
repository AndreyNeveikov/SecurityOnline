from django.contrib import admin

from ServerActivityAnalyzer.models import (
    ServerResponse,
    Server,
)

admin.site.register(ServerResponse)
admin.site.register(Server)

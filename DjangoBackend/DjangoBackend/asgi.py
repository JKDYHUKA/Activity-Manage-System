"""
ASGI config for DjangoBackend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from . import routing
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
from django.urls import re_path
from chat import consumers

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoBackend.settings")

# application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),  # http走Django默认的asgi
        "websocket": URLRouter(routing.websocket_urlpatterns),  # websocket走channels
    }
)
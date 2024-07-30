# api/routing.py

from django.urls import path
from app.consumers import VoiceTOTextConsumer
from django.urls import re_path
from app import consumers

# websocket_urlpatterns = [
#     path('ws/video/', VideoConsumer.as_asgi()),
# ]

websocket_urlpatterns = [
    re_path(r'ws/video/RHIuS2FuaGFpeWFfTmF5YWs=/$', consumers.VoiceTOTextConsumer.as_asgi()),
]
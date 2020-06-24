from channels.routing import ProtocolTypeRouter
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]

# application = ProtocolTypeRouter({
#     # (http->django views is added by default)
# })
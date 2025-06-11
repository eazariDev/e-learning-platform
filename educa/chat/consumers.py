# chat/consumers.py

import json
from channels.generic.websocket import WebsocketConsumer

from asgiref.sync import async_to_sync

from django.utils import timezone

# class ChatConsumer(WebsocketConsumer):
    
#     def connect(self):
#         self.user = self.scope['user']
#         self.id = self.scope['url_route']['kwargs']['course_id']
#         self.room_group_name = f'chat_{self.id}'
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name, self.channel_name
#         )
#         self.accept()
        
        
#     def disconnect(self, close_code):
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name, self.channel_name
#         )
    
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#         now = timezone.now()
        
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,{
#                 'type': 'chat_message',
#                 'message': message,
#                 'user': self.user.username,
#                 'datetime': now.isoformat(),
#             }
#         )
        
#         # self.send(text_data=json.dumps({'message': message}))
        
        
#     def chat_message(self, event):
#         self.send(text_data=json.dumps(event))


# Fully asynchronous consumer
from channels.generic.websocket import AsyncWebsocketConsumer

from chat.models import Message

from courses.models import Course


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.user = self.scope['user']
        self.id = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = 'chat_%s' % self.id
        
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        
        await self.accept()
        
        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )
    

    async def persist_message(self, message):
        await Message.objects.acreate(
            user=self.user, course_id=self.id, content=message
        )


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        now = timezone.now()
        
        await self.channel_layer.group_send(
            self.room_group_name,{
                'type': 'chat_message',
                'message': message,
                'user': self.user.username,
                'datetime': now.isoformat(),
            }
        )
        
        await self.persist_message(message)        
        # self.send(text_data=json.dumps({'message': message}))
        
        
    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))
   
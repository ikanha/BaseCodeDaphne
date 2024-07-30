from channels.generic.websocket import AsyncWebsocketConsumer




class VoiceTOTextConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("connected")
        await self.accept()
        print("accepted")

    async def disconnect(self, close_code):
        print("disconnected")
        pass

    async def receive(self, text_data):
        print("received")
        print(text_data)
        pass
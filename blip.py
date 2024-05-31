import asyncio

from lime_transport_websocket import WebSocketTransport
from blip_sdk import ClientBuilder

IDENTIFIER = 'devagenermain'
ACCESS_KEY = 'SVFtRnhzOTMyRjVnOFB0ZmUySUU='

async def main_async() -> None:
    # Create a client instance passing the identifier and access key of your chatbot
    client = ClientBuilder() \
        .with_identifier(IDENTIFIER) \
        .with_access_key(ACCESS_KEY) \
        .with_transport_factory(lambda: WebSocketTransport()) \
        .build()

    # Connect with the server asynchronously
    # Connection will occurr via websocket on the 8081 port
    await client.connect_async()
    print('Application started. Press Ctrl + c to stop.')

loop = asyncio.get_event_loop()
loop.run_until_complete(main_async())
loop.run_forever()
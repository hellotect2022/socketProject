import asyncio
import websockets

# 연결된 모든 클라이언트를 저장하는 리스트
connected_clients = set()

async def chat_server(websocket, path):
    try:
        # 클라이언트가 연결될 때마다 클라이언트를 저장
        connected_clients.add(websocket)

        async for message in websocket:
            # 연결된 모든 클라이언트에게 메시지 전송
            for client in connected_clients:
                print("get message",message)
                await client.send(message)
    except websockets.exceptions.ConnectionClosedError:
        pass
    finally:
        # 클라이언트가 연결을 종료하면 클라이언트를 제거
        connected_clients.remove(websocket)

start_server = websockets.serve(chat_server, "0.0.0.0", 7777)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
import asyncio
import websockets

async def hello():
    #uri = "ws://127.0.0.1:7777"
    uri = "ws://hellotect2022.synology.me:9380"
    async with websockets.connect(uri) as websocket:
        print("fff",websocket)
        # 서버로 hello 전달
        while True:
            message = input("메시지를 입력하세요:")
            if message == "exit":
                break
            await websocket.send(message)
            response = await websocket.recv()
            print(f"서버로부터 받은 응답: {response}")

asyncio.get_event_loop().run_until_complete(hello())
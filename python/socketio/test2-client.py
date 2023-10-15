import socketio
import asyncio
import time

sio_client = socketio.AsyncClient(logger=False, engineio_logger=False)

@sio_client.event()
async def connect():
    print('I\'m connected')

@sio_client.event()
async def disconnect():
    print('I\'m disconnected')

@sio_client.event()
async def message(data):
    print(f'return from server {data}')

async def main():

    try:
        await sio_client.connect(
            url='http://localhost:7777',
            socketio_path='sockets')

        while sio_client.connected :
            message = input("값을 입력하세요 (나가기 :exit) :")
            if message =='exit':
                await sio_client.disconnect()
                break
            
            await sio_client.emit("message",message)
    except Exception as e:
        print(f"이벤트 전송 중 오류 발생: {e}")


    await sio_client.disconnect()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
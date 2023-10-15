import socketio
from fastapi import FastAPI
import uvicorn


sio_server = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=[]
)

sio_app = socketio.ASGIApp(
    socketio_server=sio_server,
    socketio_path='/sockets'
)

app=FastAPI()
app.mount('/', app=sio_app)

@app.get('/')
async def home():
    return {'message': 'Hello developers'}


@sio_server.event 
async def connect(sid, env, auth):
    print(f"{sid} client connected!!")
    try:
        await sio_server.emit('message','client is connected')
    except Exception as e:
        print(f"이벤트 전송 중 오류 발생: {e}")

@sio_server.event 
async def disconnect(sid, env, auth):
    print(f"{sid} client disconnected!!")

@sio_server.event
async def message(sid,data):
    print(f'message id {sid}, and data is {data}')

if __name__ == '__main__':
    uvicorn.run('test2-server:app', host='0.0.0.0', port=7777, reload=True)
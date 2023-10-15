from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import socketio
#from fastapi_socketio import SocketManager
import uvicorn

#FastAPI 앱 생성
app = FastAPI()

# Socket.IO 서버 생성 
sio = socketio.AsyncServer(cors_allowed_origins="*")
# WebSocket 경로에 대한 핸들러 함수
async def socketio_endpoint(scope, receive, send):
    await sio.handle_request(scope, receive, send)

# WebSocket 경로 라우트 추가
app.add_websocket_route(socketio_endpoint, "/socket.io/")

# FastAPI 경로 핸들러
@app.get("/", response_class=HTMLResponse)
async def read_root():
    # 클라이언트에게 전달할 HTML 파일
    return """
    <html>
    <head>
        //<script src="https://cdn.socket.io/4.2.2/socket.io.min.js"></script>
        <script>
            var socket = io.connect('http://localhost:8080/socket.io/');
            socket.on('message', function(data) {
                console.log('서버로부터 메시지 수신:', data);
            });
        </script>
    </head>
    <body>
        FastAPI와 Socket.IO를 사용한 실시간 통신 예제입니다.
    </body>
    </html>
    """

# Socket.IO 이벤트 핸들러
@sio.event
async def message(sid, data):
    print('클라이언트로부터 메시지 수신:', data)
    # 클라이언트에게 메시지 전송
    await sio.emit('message', '서버로부터 메시지: ' + data)


if __name__ == '__main__':
    uvicorn.run("test:app", host='0.0.0.0', port=8080, reload=True, debug=False)
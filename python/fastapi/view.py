from fastapi import APIRouter
from fastapi.responses import HTMLResponse

viewRouter= APIRouter()

@viewRouter.get("/")
async def view_root():
    return {"message": "Hello, view root"}

@viewRouter.get("/login", response_class=HTMLResponse)
async def view_login():
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>두두 웹톡</title>
        <link rel="stylesheet" href="/static/css/style.css"> <!-- CSS 파일을 연결 -->
    </head>
    <body>
        <div class="container">
            <h1>로그인</h1>
            <form action="/register" method="post">
                <label for="username">아이디:</label>
                <input type="text" id="username" name="username" required>
                <br>
                <label for="password">비밀번호:</label>
                <input type="password" id="password" name="password" required>
                <br>
                <button type="submit">로그인</button>
            </form>
            <p>회원이 아니신가요? <a href="/view/signup">회원가입</a>하러 가기</p>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@viewRouter.get("/signup", response_class=HTMLResponse)
async def view_signup():
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>두두 웹톡</title>
        <link rel="stylesheet" href="/static/css/style.css"> <!-- CSS 파일을 연결 -->
    </head>
    <body>
        <div class="container">
            <h1>회원가입</h1>
            <form action="/register" method="post">
                <label for="username">아이디:</label>
                <input type="text" id="username" name="username" required>
                <br>
                <label for="password">비밀번호:</label>
                <input type="password" id="password" name="password" required>
                <br>
                <button type="submit">가입</button>
            </form>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
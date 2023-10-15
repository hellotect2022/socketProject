from fastapi import APIRouter
from dto import SignUpDto, LoginDto
import redis
import json

apiRouter = APIRouter()

# Redis 클라이언트 생성
redis_client = redis.Redis(host='localhost', port=6379, db=0)

@apiRouter.get("/")
async def api_root():
    return {"message": "Hello, api root"}

@apiRouter.post("/signUp")
async def api_sighUp(signUpDto:SignUpDto):
    redis_client.hset("user",signUpDto.id,signUpDto.json())
    return signUpDto

@apiRouter.post("/login")
async def api_logIn(loginDto:LoginDto):
    user_redis = redis_client.hget("user",loginDto.id)
    user = json.loads(user_redis)
    if user["id"] == loginDto.id and user["pw"] == loginDto.pw:
        return {"message":"login successfully!!"}
    else :
        return {"message":"login error"}
    

# @router.get("/items/{item_id}")
# async def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}


from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
from api import apiRouter
from view import viewRouter


app=FastAPI()
app.include_router(apiRouter, prefix="/api")
app.include_router(viewRouter, prefix="/view")
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ =="__main__":
    uvicorn.run('main:app',host='0.0.0.0',port=8080,reload=True)
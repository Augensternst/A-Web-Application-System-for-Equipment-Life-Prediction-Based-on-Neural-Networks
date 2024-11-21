import subprocess
from fastapi import FastAPI, File, Form, Request, status, Depends
from jose import ExpiredSignatureError
from common.CommonResponse import CommonResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from tortoise.exceptions import DoesNotExist
from tortoise.contrib.fastapi import register_tortoise
from database.config import CONFIG

from database.models import User
from tools.security import get_current_user, is_expired
from starlette.exceptions import HTTPException as StarletteHTTPException

from api.user import userAPI
from api.mmodel import modelAPI
from api.component import componentAPI
from api.data import dataAPI

uploaded_files_md5s = {}


class Item(BaseModel):
    data: str


class PieData(BaseModel):
    value: float
    name: str


app = FastAPI()
register_tortoise(app=app,
                  config=CONFIG,
                  generate_schemas=True,  # 是否自动生成表结构
                  )
app.include_router(userAPI, prefix="/user", tags=["用户相关API"])
app.include_router(modelAPI, prefix="/model", tags=["模型相关API"])
app.include_router(componentAPI, prefix="/component", tags=["组件相关API"])
app.include_router(dataAPI, prefix="/data", tags=["数据相关API"])


@app.middleware("http")
async def token_expired_generate(request: Request, call_next):
    # 如果token过期, 产生新的token
    bearer_token = request.headers.get("Authorization")
    response = await call_next(request)
    if bearer_token:
        token = bearer_token.split(" ")[1]
        new_token = is_expired(token)
        if new_token:
            response.set_cookie("Authorization", new_token)
            return response
    return response




@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    # 处理 HTTPException 异常
    return CommonResponse.error(exc.status_code, exc.detail)


@app.exception_handler(DoesNotExist)
async def does_not_exist_exception_handler(request, exc):
    return CommonResponse.error(404, "资源不存在")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/current_user")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", host="localhost", port=8000, reload=True)

from fastapi import status
from fastapi.responses import JSONResponse, Response
from typing import Union
import json
from json import JSONEncoder as JSONR
from database.models import User, MModel, Component, DData
import datetime

class CommonResponse:
    @staticmethod
    def success(data, message: str = "success") -> JSONResponse:
        cls = Myncoder
        content = json.dumps({
            "code": 200,
            "message": message,
            "data": data
        }, cls=cls, ensure_ascii=False)
        return Response(content=content, status_code=status.HTTP_200_OK, media_type="application/json")

    @staticmethod
    def error(code: int, message: str) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "code": code,
                "message": message,
                "data": None
            }
        )

    @staticmethod
    def custom(status_code: int, code: int, message: str, data: Union[dict, list, str] = None) -> JSONResponse:
        return JSONResponse(
            status_code=status_code,
            content={
                "code": code,
                "message": message,
                "data": data
            }
        )

    @staticmethod
    def response(status_code: int, code: int, message: str, data: Union[dict, list, str] = None) -> JSONResponse:
        return JSONResponse(
            status_code=status_code,
            content={
                "code": code,
                "message": message,
                "data": data
            }
        )


class Myncoder(JSONR):
    def default(self, o):
        if isinstance(o, Component):
            return {
                "id": o.id,
                "name": o.name,
                "status": o.status,
                "life_forecast": o.life_forecast,
                "location": o.location,
                "updated_time": o.updated_time.strftime('%Y-%m-%d %H:%M:%S'),
                "model_name": o.model.name if isinstance(o.model, MModel) else None,
                "model_id": o.model.id if isinstance(o.model, MModel) else None,
            }
        if isinstance(o, DData):
            return {
                "id": o.id,
                "name": o.name,
                "time": o.time,
                "result": o.result,
                "component_name": o.component.name if isinstance(o.component, Component) else None,
                "component_id": o.component.id if isinstance(o.component, Component) else None
            }
        if isinstance(o, MModel):
            return {
                "id": o.id,
                "name": o.name,
                "style": o.style,
                "uploaded_time": o.uploaded_time.strftime('%Y-%m-%d %H:%M:%S'),
                "status": o.status,
                "description": o.description,
                "md5": o.md5,
                "user": o.user.username if o.user else None
            }
        if isinstance(o, datetime.datetime):
            # 转化成东八区时间
            o = o + datetime.timedelta(hours=8)
            return o.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(o, list):
            return [self.default(i) for i in o]
        if isinstance(o, dict):
            return {k: self.default(v) for k, v in o.items()}
        return super().default(o)

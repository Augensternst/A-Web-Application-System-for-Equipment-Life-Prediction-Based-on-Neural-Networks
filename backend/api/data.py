from fastapi import UploadFile, Form, Depends, Response
from common.CommonResponse import CommonResponse
from tools.security import get_current_user
from fastapi import APIRouter
from database.models import DData, Component
from common.CommonResponse import CommonResponse
from tortoise.exceptions import DoesNotExist
dataAPI = APIRouter()


@dataAPI.post("/", description="上传数据")
async def create_data(file: UploadFile, name: str = Form(...), component: int = Form(...), current_user=Depends(get_current_user)):
    """
    上传用户的指定组件的数据至数据库

    Args:
    - file: 上传的文件
    - name: 数据名称
    - component: 组件id
    - current_user: 当前用户, 由Depends(get_current_user)注入, 即需要在请求头中携带token

    Returns:
    - 成功: 返回数据id
    - 失败: 返回错误信息
    """
    try:
        component = await Component.get(id=component).prefetch_related('user')
    except DoesNotExist:
        return CommonResponse.error(104, "组件不存在")
    if not component:
        return CommonResponse.error(104, "组件不存在")
    if component.user != current_user:
        return CommonResponse.error(124, "无权访问其它用户的组件信息")
    data = await DData.create(
        file=await file.read(),
        name=name,
        component=component
    )
    return CommonResponse.success(data.id)


@dataAPI.get("/user_component/{id}", description="返回当前用户下的某个组件的数据", response_model_exclude={"file"})
async def read_user_component_data(id: int, current_user=Depends(get_current_user)):
    component = await Component.get(id=id).prefetch_related('user')
    if not component:
        return CommonResponse.error(104, "组件不存在")
    if component.user != current_user:
        return CommonResponse.error(124, "无权访问其它用户的组件信息")
    datas = await DData.filter(component=component)
    for d in datas:
        d.file = ''
    return datas


@dataAPI.get("/download/{id}", description="下载数据")
async def download_data(id: int, current_user=Depends(get_current_user)):
    data = await DData.get(id=id).prefetch_related('component__user')
    if not data:
        return CommonResponse.error(105, "数据不存在")
    if data.component.user != current_user:
        return CommonResponse.error(125, "无权下载其它用户的数据")
    return Response(content=data.file, media_type="application/octet-stream", headers={"Content-Disposition": f"attachment; filename={data.name}"})


@dataAPI.get("/all_user", description="返回当前用户下的所有数据", response_model_exclude={"file"})
async def read_user_data(current_user=Depends(get_current_user)):
    datas = await DData.filter(component__user=current_user).prefetch_related('component').values('id', 'name', 'time', 'result', 'component_id', 'component__name')
    return CommonResponse.success(datas)


@dataAPI.delete("/{id}", description="删除数据")
async def delete_data(id: int, current_user=Depends(get_current_user)):
    data = await DData.get(id=id).prefetch_related('component__user').values('id', 'component__user__username')
    if data['component__user__username'] != current_user.username:
        return CommonResponse.error(125, "无权删除其它用户的数据")
    delete_count = await DData.filter(id=id).delete()
    if delete_count == 0:
        return CommonResponse.error(500, "删除失败")
    return CommonResponse.success("删除成功")

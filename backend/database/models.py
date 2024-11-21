from tortoise.models import Model
from tortoise import fields

class User(Model):
    username = fields.CharField(pk=True, max_length=50, description="用户名")
    hashed_password = fields.CharField(max_length=128, description="密码")
    email = fields.CharField(max_length=50, description="邮箱")
    phone = fields.CharField(max_length=50, description="电话")
    role = fields.IntField(description="角色", default=0)
    avatar = fields.BinaryField(description="头像", null=True)
    # 与model的一对多关系
    models: fields.ReverseRelation['MModel']


class MModel(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, description="模型名称", unique=True)
    style = fields.CharField(
        max_length=50, description="模型风格", default="default")
    uploaded_time = fields.DatetimeField(auto_now_add=True, description="上传时间")
    status = fields.CharField(
        max_length=10, description="模型状态", default="未知")
    description = fields.TextField(description="描述")
    modelfile = fields.BinaryField(description="模型文件")
    md5 = fields.CharField(max_length=32, description="md5值", unique=True)
    user = fields.ForeignKeyField(
        'models.User', related_name='models', description="用户", null=True)
    # 与component的一对多关系
    components: fields.ReverseRelation['Component']


class Component(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, description="组件名称")
    status = fields.IntField(description="组件状态", null=True)
    life_forecast = fields.IntField(description="寿命预测", default=-1)
    location = fields.CharField(max_length=50, description="位置")
    updated_time = fields.DatetimeField(auto_now_add=True, description="更新时间")
    pic = fields.BinaryField(description="图片", null=True)
    model = fields.ForeignKeyField(
        'models.MModel', related_name='components', description="模型", null=True)
    user = fields.ForeignKeyField(
        'models.User', related_name='components', description="用户")
    description = fields.TextField(description="描述", null=True)
    # 与data的一对多关系
    data: fields.ReverseRelation['DData']


class DData(Model):
    id = fields.IntField(pk=True)
    file = fields.BinaryField(description="数据文件")
    name = fields.CharField(max_length=50, description="数据名称", null=True)
    time = fields.DatetimeField(auto_now_add=True, description="上传时间")
    result = fields.TextField(description="结果", null=True)
    component = fields.ForeignKeyField(
        'models.Component', related_name='data', description="组件")

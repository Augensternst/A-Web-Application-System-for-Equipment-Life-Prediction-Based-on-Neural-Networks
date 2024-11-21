# backend

## 配置开发环境
### 安装依赖
+ pip install fastapi
+ pip install "uvicorn[standard]”
+ pip install tortoise-orm
+ pip install python-jose
+ pip install passlib
+ pip install python-multipart
+ pip install aiomysql
+ pip install aerich
+ pip install bcrypt
### 配置orm
+ aerich init -t database.config.CONFIG # 初始化配置文件
+ aerich init-db # 初始化数据库, 一般在第一次使用时执行
+ aerich migrate [--name] (标记修改操作) #  更新操作并生成迁移文件
+ aerich upgrade # 更新数据库
+ aerich downgrade # 回滚数据库
+ aerich history # 查看历史操作

### 配置身份验证


### 查看swagger
> http://127.0.0.1:8000/docs
>
### 启动服务
> uvicorn main:app --reload

### 响应状态码定义
+ 100-109：模型相关
+ 110-119：组件相关
+ 120-129：用户相关
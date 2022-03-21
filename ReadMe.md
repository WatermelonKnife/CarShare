## 瓜大校园拼车助手

### 演示视频
[哔哩哔哩](https://www.bilibili.com/video/BV1Ta411k7XH/)

#### 软件使用方法与入口:

1. 在运行前,先配置mysql环境,运行mysqlBackups.sql备份文件建立数据库, 并在operating/dbop.py下,

修改自己的数据库名称和密码,之后即可成功连接数据库.

2. 配置python3.8环境,导入要用的包,找到operating/LoginOp.py , 使用python解释器运行即可开始运行.

3. 程序入口./operating/LoginOp.py

#### 运行环境:

python3.8 , PyQt5 , pymysql , hashlib

#### 功能实现:

1. 路线管理

> 增删改查路线

2. 司机管理

> 增删改查司机信息

3. 拼车管理

> 司机实现发布拼车单,删改拼车单
>
> 用户实现参与拼车
>
> 拼车可行性检查

4. 用户管理

> 注册,登录, 密码MD5 加密存储
>
> 不同类型用户赋予不同权限

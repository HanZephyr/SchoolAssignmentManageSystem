# 作业管理系统（SchoolAssignmentManageSystem）

[![My Blog](https://img.shields.io/badge/Blog-lifepoem-orange.svg?style=flat-square)](http://www.lifepoem.cn/) [![Python Version](https://img.shields.io/badge/Python-3.6|3.7|3.8-success.svg?style=flat-square)](https://www.python.org/) [![Release latest](https://img.shields.io/badge/Release-latest-blue.svg?style=flat-square)](https://github.com/allwaysLove/ChaoXing-Automatic-watch-Course/releases) [![MIT License](https://img.shields.io/badge/LICENSE-MIT-yellow.svg?style=flat-square)](https://github.com/allwaysLove/ChaoXing-Automatic-watch-Course/blob/master/LICENSE)



## :bulb: 简介

**[SchoolAssignmentManageSystem](https://github.com/allwaysLove/SchoolAssignmentManageSystem)** 一款基于 **Python3 与 Django WEB框架** 的作业管理系统，提供作业管理及查询服务



## :sparkling_heart: 作者

| Author                                     | E-mail                                               | Blog                                             |
| ------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------ |
| [冬酒暖阳](https://github.com/allwaysLove) | [mailto:1067764354@qq.com](mailto:1067764354@qq.com) | [博客：www.lifepoem.cn](https://www.lifepoem.cn) |

## :postal_horn: 界面展示

1. 后台管理界面

    ![image-20200626121647852](https://cos.lifepoem.cn/assignments/imgs/20200626121657.png)

2. 作业管理页面

    ![image-20200626134401797](https://cos.lifepoem.cn/assignments/imgs/20200626134401.png)

3. 获取接口简单使用说明

    ![image-20200626133850532](https://cos.lifepoem.cn/assignments/imgs/20200626133850.png)

## :hammer: 安装

1. 通过源代码安装

    ```shell
    git clone https://github.com/allwaysLove/SchoolAssignmentManageSystem
    python -m pip install -r requirements.txt
    ```




## :blue_book: ​使用

1. 使用命令行 cd 到项目根目录

2. 执行以下命令

    ```shell
    # 创建超级用户（管理员）
    python manage.py makesuperuser
    # 依据模型迁移构建数据库表
    python manage.py makemigrations SchoolAssignmentListManage
    python manage.py migrate
    ```

3. 使用 runserver 命令开启服务器

    ```shell
    python manage.py runserver 0.0.0.0:8000
    ```

4. 随后便可在本地浏览器访问 http://localhost:8000/admin 看到作业管理系统



## :memo: 目录结构及文件注释

```
SchoolAssignmentManageSystem/
├────.gitignore  # git 忽略文件
├────LICENSE  # MIT授权文件
├────manage.py  # Django 项目命令工具
├────README.md  # 项目文档
├────requirements.txt  # 项目代码主要依赖库
├────SchoolAssignmentListManage/  # 应用目录
│    ├────__init__.py
│    ├────admin.py
│    ├────apps.py
│    ├────diy_widgets.py
│    ├────models.py  # 数据库模型
│    ├────templates/
│    │    ├────add.png
│    │    └────image_multi_upload.html
│    ├────tests.py
│    ├────urls.py  # 应用路由配置
│    └────views.py  # 视图
└────SchoolAssignmentManageSystem/
     ├────__init__.py
     ├────settings.py  # Django项目配置
     ├────urls.py  # 项目路由配置
     └────wsgi.py
```



## :bookmark_tabs:版本更新日志

> ### [1.0.0] - 2020-03-26
> #### 项目1.0版本
> * 课程名称编辑
> * 作业管理（增删改查）
> * 通过接口获取 JSON 格式作业数据
> * 美观的后台管理界面



## :clipboard: ​To-Do List

- [ ] 完成课表配置，增加课表管理功能



## :bookmark_tabs: License

[MIT © 2020 冬酒暖阳](https://github.com/allwaysLove/SchoolAssignmentManageSystem/blob/master/LICENSE)


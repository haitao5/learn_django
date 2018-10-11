# learn_django
learn about the django by a project

## 说明
本工程根据[runoob教程](http://www.runoob.com/django/django-tutorial.html)，使用版本为Python 3.7 和Django 2.1.0，部分内容与教程有如下差别：
1. python 版本和 django版本
2. 使用虚拟环境隔离版本
3. 创建工程时增加句号适配文件结构




## 环境安装
 
#### Python 安装
  Python 安装注意添加环境变量

#### Django 安装
  使用Pip 安装： 
*pip install django*


## 过程记录
#### 创建虚拟环境
  1. 创建 learn_django 文件夹
  2. 在 learn_django 文件夹中执行：*python -m venv py_env*
  3. 运行 *py_env\Scripts\activate*，激活虚拟环境
  4. url映射时，除按照 *url()* 函数映射外增加 *path* 函数方式映射


#### 创建项目
  1. 在 learn_django 文件夹虚拟环境中执行 *django-admin.py startproject HelloWorld .* 创建工程
  2. 运行 *python manage.py runserver* 命令启动服务
  3. 在浏览器中打开 *http://127.0.0.1:8000/* 检查创建结果
  4. 目录说明：
> * manage.py: 与该 Django 项目进行交互的命令行工具。
> * HelloWorld/__init__.py: 一个空文件，告诉 Python 该目录是一个 Python 包。
> * HelloWorld/settings.py: 该项目的设置/配置。
> * HelloWorld/urls.py: 该项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
> * HelloWorld/wsgi.py: WSGI 兼容的 Web 服务器的入口，以便运行你的项目。




## 总结

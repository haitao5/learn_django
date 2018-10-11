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
  5. 使用默认的SQLite替换MySQL



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


#### 创建视图
  1. 在HelloWorld目录新建 view.py 文件
  2. 在HelloWorld/urls.py 文件中将URL与视图函数进行绑定

#### 应用模板
  1. 创建模板目录和文件templates/hello.html
  2. 在HelloWorld/settings.py 文件增加模板路径为：'DIRS': [BASE_DIR+"/templates",],
  3. 在view.py，增加一个新的对象，render 还使用了一个字典 context 作为参数向模板提交数据
  4. 访问网址http://127.0.0.1:8000/hello


#### 模板继承
  1. 创建模板文件templates/base.html 
  2. 更新templates/hello.html 文件，并传入参数


#### 创建APP







## 总结
### Django 模板标签
#### if/else 标签
  {% if %} 标签接受 and ， or 或者 not 关键字来对多个变量做判断 ，或者对变量取反（ not )
``` html
{% if condition1 %}
   ... display 1
{% elif condition2 and condition3 %}
   ... display 2
{% else %}
   ... display 3
{% endif %}
```

#### ifequal/ifnotequal 标签

```
{% ifequal section 'sitenews' %}
    <h1>Site News</h1>
{% else %}
    <h1>No News Here</h1>
{% endifequal %}
```

#### for 标签
  给标签增加一个 reversed 使得该列表被反向迭代
```
{% for athlete in athlete_list %}
    <h1>{{ athlete.name }}</h1>
    <ul>
    {% for sport in athlete.sports_played reversed  %}
        <li>{{ sport }}</li>
    {% endfor %}
    </ul>
{% endfor %}
```

#### include 标签
  {% include %} 标签允许在模板中包含其它的模板的内容。
```
{% include "nav.html" %}
```

#### 注释标签
```
{# 这是一个注释 #} 
```

#### 过滤器
  模板过滤器可以在变量被显示前修改它，过滤器使用管道字符

```
{{ my_list|first|upper }}
{{ bio|truncatewords:"30" }}
```
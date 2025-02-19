@echo off
REM 设置 Django 的配置文件路径
set DJANGO_SETTINGS_MODULE=myprojectServer.settings

REM 设置静态文件和模板文件路径
set STATIC_ROOT=static
set TEMPLATES_DIR=templates

REM 启动 Django 服务器
.\my_django_app.exe runserver --noreload

REM 暂停，以便查看输出
pause
import os
import PyInstaller.__main__
from pathlib import Path

# 项目根目录
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR =Path(__file__).resolve().parent

# PyInstaller 配置
PyInstaller.__main__.run([
    'manage.py',  # 入口文件
    '--name=my_django_app',  # 可执行文件名称
    # '--onefile',  # 打包为单个可执行文件
    '--add-data', f'{os.path.join(BASE_DIR, "myprojectServer", "settings.py")}:myprojectServer',  # 添加 settings.py
    '--add-data', f'{os.path.join(BASE_DIR, "static")}:static',  # 添加静态文件
    '--add-data', f'{os.path.join(BASE_DIR, "templates")}:templates',  # 添加模板文件
    '--add-data', f'{BASE_DIR / 'db.sqlite3'}:.',  # 添加模板文件
    '--hidden-import=django.core.management',  # 显式导入 Django 模块
    '--hidden-import=django.core.handlers.wsgi',
    '--hidden-import=django.core.handlers.asgi',
    '--hidden-import=django.utils.autoreload',
    
    # '--hidden-import=django.db.backends.sqlite3',
    # '--hidden-import=corsheaders.context_processors',
    # '--hidden-import=django.contrib.staticfiles.templatetags',
    # '--hidden-import=willaTestApp.templatetags',
    # '--hidden-import=django.contrib.messages.templatetags',
    # '--hidden-import=django.contrib.sessions.context_processors',
    # '--hidden-import=django.contrib.contenttypes.context_processors',
    # '--hidden-import=willaTestApp.context_processors',
    # '--hidden-import=django.contrib.admin.context_processors',
    # '--hidden-import=django.contrib.auth.templatetags',
    # '--hidden-import=django.contrib.staticfiles.context_processors',
    # '--hidden-import=corsheaders.templatetags',
    # '--hidden-import=rest_framework.context_processors',
    # '--hidden-import=django.contrib.contenttypes.templatetags',
    # '--hidden-import=django.contrib.sessions.templatetags',
    # '--hidden-import=django.db.backends.__pycache__.base',

    '--clean',  # 清理临时文件
])
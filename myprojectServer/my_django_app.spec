# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['manage.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\willa\\Desktop\\FrameWork\\V2.0\\myprojectServer\\myprojectServer\\settings.py', 'myprojectServer'), ('C:\\Users\\willa\\Desktop\\FrameWork\\V2.0\\myprojectServer\\static', 'static'), ('C:\\Users\\willa\\Desktop\\FrameWork\\V2.0\\myprojectServer\\templates', 'templates'), ('C:\\Users\\willa\\Desktop\\FrameWork\\V2.0\\myprojectServer\\db.sqlite3', '.')],
    hiddenimports=['django.core.management', 'django.core.handlers.wsgi', 'django.core.handlers.asgi', 'django.utils.autoreload'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='my_django_app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='my_django_app',
)

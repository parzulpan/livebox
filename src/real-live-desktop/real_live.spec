# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['real_live.py'],
             # 设置源码路径，需要根据自己的环境来更改
             pathex=['/Users/parzulpan/Personal/GitHub/real-live/src/real-live-desktop'],
             binaries=[],
             # 添加额外的文件，以启用，目前改为脚本添加
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='real_live',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          # 设置应用图标路径，需要根据自己的环境来更改
          console=False , icon='/Users/parzulpan/Personal/GitHub/real-live/src/real-live-desktop/resources/img/logo@48x48.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='real_live')

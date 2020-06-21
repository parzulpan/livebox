# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['real_live.py'],
             pathex=['E:\\projects\\GitHub\\real-live'],
             binaries=[],
             datas=[('docs', 'docs'), ('resources', 'resources'), ('_license', '_license'), ('bin', 'bin')],
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
          name='网络直播聚合平台V1.1.0',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='E:\\projects\\GitHub\\real-live\\resources\\img\\logo@48x48.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='real_live')

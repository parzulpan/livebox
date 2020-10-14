# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# 请修改为自己的环境
# 請修改為自己的環境
# Please modify it to your own environment
Src_Path = '/Users/parzulpan/Personal/GitHub/real-live/src/real-live-desktop'

Main = [Src_Path + '/real_live.py']
Name = 'RealLive'
App_Name = 'RealLive.app'
Icon = 'logo@48x48.icns'


a = Analysis(Main,
             pathex=[Src_Path],
             binaries=[],
             datas=[(Src_Path + '/resources', 'resources'), (Src_Path + '/resources/pyqt5_material', 'pyqt5_material')],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name=Name,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name=App_Name,
             icon=Icon,
             bundle_identifier=None,
 )

# -*- mode: python -*-

block_cipher = None


a = Analysis(['app.py'],
             pathex=['/Users/ashikawa/work/GIGASELFIE_APP/100_dev/00_experiment/02_qt_opencv'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='app',
          debug=False,
          strip=False,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name='app.app',
             icon=None,
             bundle_identifier=None)

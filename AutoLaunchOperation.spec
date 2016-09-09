# -*- mode: python -*-

block_cipher = None


a = Analysis(['AutoLaunch.py'],
             pathex=['D:\Python35\Lib',
                     'D:\Python35\Lib\site-packages'],
             binaries=None,
             datas=[('D:\\PycharmWorkspace\\Meilele_Automate\\DataSource','.\\DataSource'),
                    ('D:\\PycharmWorkspace\\Meilele_Automate\\Driver','.\\Driver'),
                    ('D:\\PycharmWorkspace\\Meilele_Automate\\Image','.\\Image'),
                    ('D:\PycharmWorkspace\Meilele_Automate\config.ini',''),
					('D:\PycharmWorkspace\Meilele_Automate\TestCase',''),
					('D:\PycharmWorkspace\Meilele_Automate\Lib',''),],
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
          exclude_binaries=True,
          name='AutoLaunch',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='AutoLaunch')

# -*- mode: python -*-

block_cipher = None


a = Analysis(['AutoLaunchOperation.py'],
             pathex=['D:\\PycharmWorkspace\\Meilele_Automate', 
                     'D:\\Python35\\Lib\\site-packages'],
             binaries=[('api-ms-win-crt-utility-l1-1-0.dll','C:\\Windows\\System32\\api-ms-win-crt-utility-l1-1-0.dll','BINARY')],
             datas=[('D:\\PycharmWorkspace\\Meilele_Automate\\DataSource','.\\DataSource'),
                    ('D:\\PycharmWorkspace\\Meilele_Automate\\Driver','.\\Driver'),
                    ('D:\\PycharmWorkspace\\Meilele_Automate\\Image','.\\Image')],
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
          name='AutoLaunchOperation',
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
               name='AutoLaunchOperation')

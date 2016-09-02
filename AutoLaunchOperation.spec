# -*- mode: python -*-

block_cipher = None


a = Analysis(['D:\PycharmWorkspace\Meilele_Automate\AutoLaunchOperation.py'],
             pathex=['D:\Python35\Lib',
                     'D:\Python35\Lib\site-packages',
                     'D:\PycharmWorkspace\Meilele_Automate\selenium'],
             binaries=None,
             datas=[('D:\\PycharmWorkspace\\Meilele_Automate\\DataSource','.\\DataSource'),
                    ('D:\\PycharmWorkspace\\Meilele_Automate\\Driver','.\\Driver'),
                    ('D:\\PycharmWorkspace\\Meilele_Automate\\Image','.\\Image'),
                    ('D:\PycharmWorkspace\Meilele_Automate\config.ini','')],
             hiddenimports=['selenium.webdriver.common.utils',
                            'selenium.webdriver.support.wait',
                            'selenium.webdriver.common.desired_capabilities',
                            'selenium.common.exceptions',
                            'selenium.webdriver.support',
                            'email.mime.text',
                            'email.mime.multipart',
                            'email.header',
                            'selenium.webdriver.common.by'],
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

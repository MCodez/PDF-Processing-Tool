# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:\\Users\\lalit\\OneDrive\\Desktop\\PyQt5\\pdf_processor.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

a.datas += [('gui_icon.png','C:\\Users\\lalit\\OneDrive\\Desktop\\PyQt5\\gui_icon.png','DATA'),('pdf_tool.ui','C:\\Users\\lalit\\OneDrive\\Desktop\\PyQt5\\pdf_tool.ui','DATA')] 

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='PDF-Processor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='C:\\Users\\lalit\\OneDrive\\Desktop\\PyQt5\\gui_icon.ico',
)

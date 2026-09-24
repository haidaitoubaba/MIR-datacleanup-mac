# From the package folder: python -m PyInstaller --distpath Build/dist --workpath Build/work "Source/MIR Cleanup.spec"
from pathlib import Path
from PyInstaller.utils.hooks import collect_data_files
root = Path(SPECPATH)
a = Analysis([str(root/'mir_cleanup_app.py')], pathex=[str(root),str(root.parent)],
    binaries=[], datas=[(str(root/'mir_cleanup_viewer.html'),'.')]+collect_data_files('plotly'),
    hiddenimports=['soil_mir_plsr_Nested_LOGO_stepwise_regions_rank_reuse','brukeropusreader'],
    runtime_hooks=[str(root/'mir_runtime_hook.py')], hookspath=[], hooksconfig={'matplotlib':{'backends':['QtAgg','Agg']}},
    excludes=['PyQt5','PyQt6','PySide2','tkinter','torch','tensorflow','IPython','notebook','pytest'],
    module_collection_mode={'scipy':'py'}, noarchive=False)
pyz = PYZ(a.pure)
exe = EXE(pyz,a.scripts,[],exclude_binaries=True,name='MIR Cleanup',debug=False,bootloader_ignore_signals=False,
          strip=False,upx=False,console=False,argv_emulation=False,target_arch=None,codesign_identity=None,entitlements_file=None)
coll = COLLECT(exe,a.binaries,a.datas,strip=False,upx=False,name='MIR Cleanup')
app = BUNDLE(coll,name='MIR Cleanup.app',icon=None,bundle_identifier='org.soilmir.cleanup',
             info_plist={'CFBundleShortVersionString':'1.2.1','NSHighResolutionCapable':True,
                'NSDownloadsFolderUsageDescription':'Read the reference workbook and MIR spectra you select for cleanup.',
                'NSDocumentsFolderUsageDescription':'Read selected inputs and save your cleanup sessions and reports.',
                'NSDesktopFolderUsageDescription':'Read selected inputs and save cleanup outputs when you choose Desktop.'})

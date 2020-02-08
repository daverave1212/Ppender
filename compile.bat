SET thisdir=%~dp0
cd /d S:
cd /d %thisdir%
pyinstaller --onefile ppender.py
xcopy /y config.cfg dist\config.cfg
echo "Done."
pause
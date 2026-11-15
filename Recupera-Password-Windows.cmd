@echo off
chcp 65001 >nul
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" goto manca
".venv\Scripts\python.exe" tools\reset_password.py
pause
exit /b
:manca
echo Prima installa il gestionale con Installa-Windows.cmd.
pause
exit /b 1

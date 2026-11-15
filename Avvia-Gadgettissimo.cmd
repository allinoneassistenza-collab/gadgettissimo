@echo off
chcp 65001 >nul
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" goto manca
".venv\Scripts\python.exe" run.py
if errorlevel 1 pause
exit /b
:manca
echo Prima esegui Installa-Windows.cmd. Per istruzioni apri docs\GUIDA.html.
pause
exit /b 1

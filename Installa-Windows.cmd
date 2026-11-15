@echo off
chcp 65001 >nul
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0tools\install_windows.ps1"
if errorlevel 1 goto errore
echo Installazione terminata.
pause
exit /b 0
:errore
echo Installazione non completata. Leggi il messaggio qui sopra e la guida.
pause
exit /b 1

@echo off
cd /d "%~dp0"
cls
echo =============================================
echo   CareContinuum Agent - Demo Server
echo =============================================
echo.
echo Starting without external Python packages...
echo.
python backend\app.py
if errorlevel 1 (
  echo.
  echo Python was not found. Install Python 3.10+ and try again.
)
pause

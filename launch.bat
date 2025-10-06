@echo off
REM Batch Watermark Remover Launcher
REM Author: AI Assistant
REM Date: 2025-10-04

echo ========================================
echo   Batch Watermark Remover - Launcher
echo ========================================
echo.

REM Change to the correct directory
cd /d "E:\SORAdes\WatermarkRemover-AI"

REM Check if venv exists
if not exist "venv\" (
    echo ERROR: Virtual environment not found!
    echo Please create venv first:
    echo   python -m venv venv
    pause
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if tkinterdnd2 is installed
python -c "import tkinterdnd2" 2>nul
if errorlevel 1 (
    echo.
    echo Installing required package: tkinterdnd2...
    pip install tkinterdnd2
    echo.
)

REM Launch the GUI
echo.
echo Starting Batch Watermark Remover GUI...
echo.
python batch_watermark_remover.py

REM If Python script exits with error
if errorlevel 1 (
    echo.
    echo ERROR: Failed to start the application!
    echo Check the error messages above.
    pause
)

REM Deactivate venv
deactivate
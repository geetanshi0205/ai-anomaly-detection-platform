@echo off
REM Patient Health Monitoring System - Setup Script
REM This script sets up the environment and runs the system

setlocal enabledelayedexpansion

cls
echo ===============================================================================
echo        PATIENT HEALTH MONITORING SYSTEM - Windows Setup
echo ===============================================================================
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please download and install Python 3.9+ from https://www.python.org
    pause
    exit /b 1
)

echo [OK] Python is installed
python --version
echo.

REM Check Kafka
tasklist | find /I "java.exe" >nul
if errorlevel 1 (
    echo [WARNING] Kafka (Java) is not running
    echo Please start Kafka first:
    echo   1. Extract Apache Kafka
    echo   2. Run: bin\windows\kafka-server-start.bat config\server.properties
    echo.
)

REM Install requirements
echo ===============================================================================
echo Installing Python Dependencies...
echo ===============================================================================
pip install -r requirements.txt

if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ===============================================================================
echo [SUCCESS] Setup Complete!
echo ===============================================================================
echo.
echo To start the system, run:
echo   python main.py
echo.
pause

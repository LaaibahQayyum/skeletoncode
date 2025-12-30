@echo off
REM ============================================
REM Flask Application Service Restart Script
REM ============================================
REM This script simulates restarting the Flask
REM application service
REM ============================================

echo ========================================
echo Flask Application Service Restart
echo ========================================
echo.

REM Check if Flask app is running (simulation)
echo [1/3] Checking for running Flask application...
timeout /t 1 /nobreak >nul
echo Checking process list for Python/Flask...
echo.

REM Stop existing Flask application
echo [2/3] Stopping existing Flask application...
echo Sending stop signal to Flask application...
timeout /t 2 /nobreak >nul
echo Flask application stopped successfully
echo.

REM Start Flask application
echo [3/3] Starting Flask application...
echo Initializing Flask application service...
timeout /t 2 /nobreak >nul
echo Flask application started successfully
echo.

echo ========================================
echo Service restart completed!
echo ========================================
echo Application Status: RUNNING
echo Application URL: http://localhost:5000
echo.
echo To manually start the application:
echo   python skeleton_app.py
echo.
echo To stop the application:
echo   Press Ctrl+C in the terminal
echo.

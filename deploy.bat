@echo off
REM ============================================
REM Flask Application Deployment Script
REM ============================================
REM This script simulates deployment by copying
REM application files to the target directory
REM ============================================

echo ========================================
echo Flask Application Deployment Script
echo ========================================
echo.

REM Set deployment directory (can be overridden)
if "%DEPLOY_DIR%"=="" set DEPLOY_DIR=C:\deployment\flask-app

echo Deployment Target: %DEPLOY_DIR%
echo.

REM Create deployment directory if it doesn't exist
echo [1/5] Creating deployment directory...
if not exist "%DEPLOY_DIR%" (
    mkdir "%DEPLOY_DIR%"
    echo Created directory: %DEPLOY_DIR%
) else (
    echo Directory already exists: %DEPLOY_DIR%
)
echo.

REM Copy main application file
echo [2/5] Copying application files...
copy /Y skeleton_app.py "%DEPLOY_DIR%\" >nul
copy /Y requirements.txt "%DEPLOY_DIR%\" >nul
echo Copied: skeleton_app.py, requirements.txt
echo.

REM Copy templates directory
echo [3/5] Copying templates directory...
if exist templates (
    xcopy /E /Y /I templates "%DEPLOY_DIR%\templates\" >nul
    echo Copied: templates directory
) else (
    echo WARNING: templates directory not found
)
echo.

REM Copy static directory
echo [4/5] Copying static directory...
if exist static (
    xcopy /E /Y /I static "%DEPLOY_DIR%\static\" >nul
    echo Copied: static directory
) else (
    echo WARNING: static directory not found
)
echo.

REM Copy instance directory (database)
echo [5/5] Copying instance directory...
if exist instance (
    xcopy /E /Y /I instance "%DEPLOY_DIR%\instance\" >nul
    echo Copied: instance directory
) else (
    echo Note: instance directory not found (will be created on first run)
)
echo.

echo ========================================
echo Deployment completed successfully!
echo ========================================
echo Application deployed to: %DEPLOY_DIR%
echo.
echo Next steps:
echo 1. Navigate to: cd %DEPLOY_DIR%
echo 2. Install dependencies: pip install -r requirements.txt
echo 3. Run application: python skeleton_app.py
echo.

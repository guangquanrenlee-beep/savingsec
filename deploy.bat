@echo off
chcp 65001 >nul
echo [0/3] Optimizing images...
python scripts/optimize-images.py
echo [1/3] Building...
cd /d D:\site\chanpintuijian
hugo --gc --minify
if errorlevel 1 (
    echo Build failed!
    pause
    exit /b 1
)
echo [2/3] Committing...
git add -A
git commit -m "更新: %date% %time%"
echo [3/3] Pushing...
git push
if errorlevel 1 (
    echo Push failed!
    pause
    exit /b 1
)
echo.
echo Deployed! Cloudflare will update in 1-2 minutes.
pause

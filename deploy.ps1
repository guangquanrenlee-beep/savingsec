# SavingSec 一键部署脚本
# 修改源文件后，运行此脚本自动构建并部署

Write-Host "[1/3] 正在构建网站..." -ForegroundColor Cyan
hugo --gc --minify
if ($LASTEXITCODE -ne 0) {
    Write-Host "构建失败！" -ForegroundColor Red
    exit 1
}
Write-Host "构建成功" -ForegroundColor Green

Write-Host "`n[2/3] 提交更改..." -ForegroundColor Cyan
git add -A
$status = git status --porcelain
if (-not $status) {
    Write-Host "没有需要提交的更改" -ForegroundColor Yellow
    exit 0
}
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
git commit -m "Auto deploy: $timestamp"

Write-Host "`n[3/3] 推送到 GitHub..." -ForegroundColor Cyan
git push

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n部署成功！Cloudflare 将在 1-2 分钟内自动更新。" -ForegroundColor Green
    Write-Host "访问: https://savingsec.com" -ForegroundColor Cyan
} else {
    Write-Host "`n推送失败，请检查网络连接和 Git 凭据。" -ForegroundColor Red
}

Write-Host "`n按任意键退出..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

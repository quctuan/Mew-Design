
# Script PowerShell: Tự động hoá việc nộp Email vào hệ thống báo cáo
# Lưu ý: BOSS có thể tạo một Shortcut cho script này trên Desktop để dùng nhanh.

$sourcePath = "$HOME\Downloads" # Thư mục mặc định khi BOSS tải file mail từ web về
$targetPath = "C:\Users\caida\gds-myvnpt-wiki\inbox_mail" # Thư mục em sẽ "canh" để làm báo cáo
$fileNamePattern = "mail_export*.xlsx" # Tìm các file Excel có tên bắt đầu bằng mail_export

# Tạo thư mục đích nếu chưa có
if (!(Test-Path $targetPath)) {
    New-Item -ItemType Directory -Path $targetPath -Force
}

# Quét và di chuyển file mới nhất
$latestFile = Get-ChildItem -Path $sourcePath -Filter $fileNamePattern | Sort-Object LastWriteTime -Descending | Select-Object -First 1

if ($latestFile) {
    Copy-Item -Path $latestFile.FullName -Destination "$targetPath\pending_recap.xlsx" -Force
    Write-Host "✅ Đã nộp file mới nhất: $($latestFile.Name) vào hệ thống!" -ForegroundColor Green
    Write-Host "🤖 Em đang bắt đầu giai đoạn phân tích và làm báo cáo cho BOSS..." -ForegroundColor Cyan
}
else {
    Write-Host "❌ Không tìm thấy file mail mới trong thư mục Downloads." -ForegroundColor Red
}

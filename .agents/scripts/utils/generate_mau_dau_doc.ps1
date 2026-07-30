
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Add()
$selection = $word.Selection

function Add-StyledText($text, $style) {
    if ($style) { $selection.Style = $style }
    $selection.TypeText($text)
    $selection.TypeParagraph()
}

# Read content from the existing markdown file with UTF8 encoding
$mdFilePath = "c:\Users\caida\gds-myvnpt-wiki\wiki\docs\mau-dau-definition.md"
if (Test-Path $mdFilePath) {
    $lines = Get-Content -Path $mdFilePath -Encoding UTF8
    foreach ($line in $lines) {
        $trimmed = $line.Trim()
        
        if ($trimmed -eq "") {
            $selection.TypeParagraph()
        }
        elseif ($trimmed.StartsWith("# ")) {
            Add-StyledText ($trimmed.Substring(2)) "Heading 1"
        }
        elseif ($trimmed.StartsWith("## ")) {
            Add-StyledText ($trimmed.Substring(3)) "Heading 2"
        }
        elseif ($trimmed.StartsWith("### ")) {
            Add-StyledText ($trimmed.Substring(4)) "Heading 3"
        }
        elseif ($trimmed.StartsWith("---")) {
            # Skip horizontal lines or add a page break if preferred
        }
        else {
            # Basic cleanup for bold/italic markdown if needed, but TypeText is literal
            $cleanLine = $line -replace '\*\*|\*', ''
            Add-StyledText $cleanLine "Normal"
        }
    }
}

$outputPath = "C:\Users\caida\Documents\Mau_Dau_Definition_2026.docx"
$doc.SaveAs([ref]$outputPath)
$doc.Close()
$word.Quit()
Write-Host "Success: $outputPath"

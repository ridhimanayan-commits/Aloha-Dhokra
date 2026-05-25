$files = Get-ChildItem -Filter *.html
foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    
    # Fix Rupee symbol
    $content = $content.Replace('â‚¹', '₹')
    
    # Fix middle dot
    $content = $content.Replace('Â·', '·')
    
    Set-Content -Path $file.FullName -Value $content -Encoding UTF8
}
Write-Output "Fixed encoding typos"

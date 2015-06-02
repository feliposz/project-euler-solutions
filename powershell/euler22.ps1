$content = Get-Content names.txt
$sorted = $content -split "," -replace """", "" | Sort-Object
$total = 0
$pos = 1
$sorted | ForEach-Object {
	$value = 0
	$_ -split "" | ForEach-Object {
		If ($_ -ge "A" -and $_ -le "Z") {
			$value += [byte][char]$_ - [byte][char]"A" + 1
		}
	}
	$pos += 1
	$total += $pos * $value
}
Write-Host $total

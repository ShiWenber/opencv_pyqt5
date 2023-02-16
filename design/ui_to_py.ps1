# 对文件夹下的所有.ui文件执行 pyuic5 -o filename.py filename.ui
Get-ChildItem -Name "*.ui" | foreach-object{$_ -replace ".ui", ""}  | foreach-object{Invoke-Expression "pyuic5 -o ui_$_.py $_.ui"}
# 将文件夹下的所有.py文件复制到src\ui目录下(自动化的界面更新)
Get-ChildItem -Name "*.py" | foreach-object{Invoke-Expression "cp $_ ..\src\ui\"}
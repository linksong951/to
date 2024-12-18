@echo off
@REM ------------------
@REM 日常启动脚本

:: 获取当前日期并移除所有非数字字符（包括斜杠和空格）
set current_date=%DATE:/=-%
:: 移除星期几信息（假设在最后，并且由一个或多个空格分隔）
for /f "tokens=1 delims= " %%a in ("%current_date%") do set clean_date=%%a
:: 定义目标路径
set targetDir=D:\Code\MyOpenSource\20240719-planning-plan\log
:: 检查目标文件夹是否存在
if exist "%targetDir%\%current_date%.md" (
    echo "1"
    cmd /c "cd /d D:\Code\MyOpenSource\20240719-planning-plan&&code ./"
) else (
    @REM 创建log.md 文件 从模版中复制过来改名
    echo "2"
    copy /Y "%targetDir%\log.md" "%targetDir%\%current_date%.md"
    @REM vscode开启这个文件夹
    cmd /c "cd /d D:\Code\MyOpenSource\20240719-planning-plan&&code ./"
)
@REM ------------------
@REM 已经结束了日常日志生成
@REM 下面进行需要的操作

exit


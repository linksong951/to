@echo off
@REM ------------------
@REM 日常启动脚本
@REM 1生成 code/to/a年月日文件  日志文件md 判断是否存在此文件夹若有跳过生成 若有几天内同时使用的项目或文件夹直接分链接过去 
@REM code 打开当日文件夹
:: 获取当前日期并移除所有非数字字符（包括斜杠和空格）
set current_date=%DATE:/=-%
:: 移除星期几信息（假设在最后，并且由一个或多个空格分隔）
for /f "tokens=1 delims= " %%a in ("%current_date%") do set clean_date=%%a
:: 定义目标路径
set targetDir=D:\Code\to\%current_date%
:: 检查目标文件夹是否存在
if exist "%targetDir%" (
    echo "1"
) else (
    cmd /c "cd /d D:\Code\to\ && mkdir "%current_date%""
    @REM 创建log.md 文件 从模版中复制过来改名
    echo "2"
    copy /Y "D:\Code\to\log.md" "%targetDir%\log.md"
)
@REM ------------------
@REM 已经结束了日常日志生成
@REM 下面进行需要的操作

pause


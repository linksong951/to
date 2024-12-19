@echo off
@REM 本脚本为 学习脚本 四大件学习  程序员导航（顺便看新闻）


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



@REM 打开程序员导航
start  "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" "https://hao.panziye.com/"
@REM 打开 王道四大件
start  "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" "https://leetcode.cn/"
start  "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" "https://www.bilibili.com/video/BV1ps4y1d73V/?spm_id_from=333.788.player.switch&vd_source=19691fef5a101eb7414a8cad489bd045&p=14"
start  "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" "https://www.bilibili.com/video/BV1YE411D7nH/?spm_id_from=333.788.videopod.episodes&vd_source=19691fef5a101eb7414a8cad489bd045&p=2"
start  "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" "https://www.bilibili.com/video/BV19E411D78Q/?spm_id_from=333.788.recommend_more_video.1&vd_source=19691fef5a101eb7414a8cad489bd045"
start  "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" "https://www.bilibili.com/video/BV1b7411N798/?spm_id_from=333.999.0.0&vd_source=19691fef5a101eb7414a8cad489bd045"
start  "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" "https://tongyi.aliyun.com/qianwen/"
start  "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" "https://kimi.moonshot.cn/chat/cthbun5o082k43r0voj0"
pause
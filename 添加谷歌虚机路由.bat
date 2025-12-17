:: 获取默认网关的接口索引和网关地址
for /f "tokens=1,2,3 delims=: " %%i in ('route print 0.0.0.0 ^| findstr "0.0.0.0"') do (
    if "%%i"=="0.0.0.0" (
        set gateway=%%j
        set interface=%%k
        goto :add route
    )
)


:add route
:: 添加静态路由
set network=34.143.152.0
set mask=255.255.255.0
route add %network% mask %mask% %interface% metric 15

:: 显示新添加的路由
echo 当前路由表:
route print %network%

pause
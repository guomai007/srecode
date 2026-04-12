c3389.exe使用简介

Code By wawa@21cn.Com  Http://www.Haowawa.Com/

c3389是一个可以显示、更改本机或远程主机终端服务端口的小程序.
它可能能帮助您节省一点时间.

程序中判断远程注册表服务被禁止,然后启动的代码部分, 是抄袭refdom的, THX!!! :)

1. 显示本地终端端口

C:\tools>c3389
=======================================================
    Change Local or Remote TermService Port Program
     Code By wawa@21cn.Com  Http://www.Haowawa.Com
=======================================================
Local  Usage: c3389 7358
Remote Usage: c3389 \\192.168.0.1 adminname password 7358

Local Host TermService Port is : 3389

2. 修改本地终端端口

C:\tools>c3389 7358
=======================================================
    Change Local or Remote TermService Port Program
     Code By wawa@21cn.Com  Http://www.Haowawa.Com
=======================================================
Local  Usage: c3389 7358
Remote Usage: c3389 \\192.168.0.1 adminname password 7358

Local Host TermService Port is : 3389
Now Local Host TermServive Port Change to : 7358

Reboot Local Host to Active!

3.显示远程主机终端端口

C:\tools>c3389 \\10.17.3.3 administrator pass123
=======================================================
    Change Local or Remote TermService Port Program
     Code By wawa@21cn.Com  Http://www.Haowawa.Com
=======================================================
Local  Usage: c3389 7358
Remote Usage: c3389 \\192.168.0.1 adminname password 7358

Connecting Remote Host ...Ok!

Remote Host TermService Port is 3389

Disconnecting Remote Host ...Ok!

4.修改远程主机终端端口

C:\tools>c3389 \\10.17.3.3 administrator pass123 7358
=======================================================
    Change Local or Remote TermService Port Program
     Code By wawa@21cn.Com  Http://www.Haowawa.Com
=======================================================
Local  Usage: c3389 7358
Remote Usage: c3389 \\192.168.0.1 adminname password 7358

Connecting Remote Host ...Ok!

Remote Host TermService Port is 3389
Now Remote TermService Port Change To 7358

Disconnecting Remote Host ...Ok!
Reboot Remote Host to Active!

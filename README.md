### XRady

------

#### 脚本简介

XRady名字取于长亭科技开发的[Xray扫描器](https://docs.xray.cool/)和[Rad浏览器爬虫](https://github.com/chaitin/rad)结合而来，其功能也是将Xray扫描器和Rad爬虫结合之，Rad爬虫爬取资产的所有URL发给Xray扫描器进行扫描，批量进行。

该脚本诞生于2020年某段时间某地市的刷洞HV\\/行动，在团队小伙伴们连续多次奋战大呼友商人人都能熬得一手好夜，心脑亦非吾等常人所能比拟之时，为减轻伙伴熬夜之苦并守住得之不易的名次（为了偷懒），故而码之，初版粗糙且需手动启用Xray，本次为第2版，BUG依然。

后面80%可能不会再更新了，毕竟需求没了而且这只是个临时产物并且还是个学习产物。

#### 使用介绍

环境：Python3、Chrome、Xray、Rad

使用到的模块(Python)：threading、subprocess、time、sys、os



将[Xray扫描器](https://docs.xray.cool/)和[Rad爬虫](https://github.com/chaitin/rad)直接解压到该脚本的路径下，也可以自己改一下Xray的路径(第23行)和Rad的路径(第42行)

理论来说脚本不受系统限制，当前只在Windows和Mac（自己改路径）上使用，暂未较大Bug



Xrady\

​	|__ xray_windows_amd64.exe\\xray_windows_amd64.exe

​	|__ rad_windows_amd64.exe\\rad_windows_amd64.exe

​	|__ Xrady.py



使用命令：`C:\xray> python Xrady.py [File Name]`

如：python Xrady.py url.txt

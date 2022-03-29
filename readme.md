# PeertoTELE

一个自动登录peer2profit查看每日收益的小工具。

基于playwright开发。

## 使用说明

需要一台本地服务器用于开图形界面手动生成cookie验证（当然你也可以直接导出cookie）。

首先安装playwright。

```
# 安装playwright库
pip install playwright

# 安装浏览器驱动文件（安装过程稍微有点慢）
python3 -m playwright install
```

打开界面，登录，生成cookie文件

```
# 注意这里设置了超时时间为10000000，默认的时间太短无法进行操作。--save-storage表示存储页面状态
python -m playwright cr https://peer2profit.com/dashboard --save-storage peer2profit --timeout 100000000 
```

将生成的文件和`run.py`文件置于同一目录下，配置`run.py`文件内的telegrambot信息。

使用`python3 run.py`开始运行。
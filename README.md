# tg-nickname-time
[案例参考](https://t.me/EXOHZI)

[机器人定制开发](https://t.me/gpt5apt)

Telegram 昵称 随时间变化

把当前时间设置为telegram昵称

运行环境：

Debian 10

Python3

每10秒，更新一次用户名（last_name）

#下载
```
git clone https://github.com/mmm-py/tg-nickname-time.git
```
#进入目录
```
cd tg-nickname-time
```
#安装依赖
```
pip3 install -r requirements.txt
```
#运行
```
python3 bot.py
```
根据提示输入 api_id 和 api_hash 。接着输入手机号和验证码，如果账号开启了二次验，证根据提示再输入二次验证的密码。最后看到 It works! 表明成功了。

api_id 和 api_hash 获取地址

1. 登录 Telegram 的 应用管理页面 (https://my.telegram.org/)

2. 点击 "API development tools" 并填写表格。其中 "App title" 和 "Short name" 可以随意填写，"Platform" 选择你的开发平台，"Description" 是对你的应用的简短描述。

3. 提交表格后，你将获得一个 "App api_id" 和 "App api_hash"。这就是你的 API ID 和 API Hash。

成功的同时，会在当前目录生成两个session文件：

api_auth.session

api_auth.session-journal

后台运行
```
nohup python3 bot.py &
```
开机自启
```
python3 -u 程序目录/bot.py > /var/log/tgusername.log 2>&1 &
```
如 python3 -u /root/tg-nickname-time/bot.py > /var/log/tgusername.log 2>&1 &

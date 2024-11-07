# -tg-nickname-time
Telegram 用户名随时间变化
把当前时间设置为telegram昵称
运行环境：

Debian 10
Python3
每10秒，更新一次用户名（last_name）
运行

#安装依赖

pip3 install -r requirements.txt

#运行

python3 bot.py

根据提示输入 api_id 和 api_hash 。接着输入手机号和验证码，如果账号开启了二次验，证根据提示再输入二次验证的密码。最后看到 It works! 表明成功了。


成功的同时，会在当前目录生成两个session文件：

api_auth.session
api_auth.session-journal

后台运行

nohup python3 bot.py &

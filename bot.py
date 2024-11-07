#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Updated:
#  1. 使用async来update lastname，更加稳定
#  2. 修改为当前时间：年-月-日-时:分 格式

import time
import os
import sys
import logging
import asyncio
from time import strftime
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

api_auth_file = 'api_auth'
if not os.path.exists(api_auth_file+'.session'):
    api_id = input('api_id: ')
    api_hash = input('api_hash: ')
else:
    api_id = 123456
    api_hash = '00000000000000000000000000000000'

client1 = TelegramClient(api_auth_file, api_id, api_hash)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def change_name_auto():
    # Set time zone to UTC+8

    print('will change name')

    while True:
        try:
            # 获取当前时间并格式化为 "年-月-日-时:分"
            time_cur = strftime(" %Y-%m-%d%H:%M 🕞️", time.localtime())  # 采用年-月-日-时:分格式
            last_name = '%s' % (time_cur)  # 更新姓氏为当前时间

            # 更新 Telegram 账户的姓氏
            await client1(UpdateProfileRequest(last_name=last_name))
            logger.info('Updated -> %s' % last_name)
        
        except KeyboardInterrupt:
            print('\nwill reset last name\n')
            await client1(UpdateProfileRequest(last_name=''))  # 重置姓氏为空
            sys.exit()

        except Exception as e:
            print('%s: %s' % (type(e), e))

        await asyncio.sleep(60)  # 每 60 秒更新一次

# main function
async def main(loop):

    await client1.start()

    # 创建新的任务
    print('creating task')
    task = loop.create_task(change_name_auto())  # 运行改变姓名的任务
    await task
     
    print('It works.')
    await client1.run_until_disconnected()  # 一直保持连接，直到断开
    task.cancel()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))

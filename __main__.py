# coding: utf-8
"""main"""
import traceback
import time
from random import randint
import itchat
from itchat.content import TEXT, FRIENDS

import config
from log import Logger


LOG = Logger('main', config.ERROR_LOG)

@itchat.msg_register(TEXT)
def text_reply(msg):
    """text"""
    try:
        time.sleep(randint(1, 3))
        itchat.send_msg(msg='经验共享平台，让我们每天都能经验+1！\n网址 http://10.9.52.233 (仅公司网络可访问，推荐使用Chrome或Firefox浏览器)',\
                            toUserName=msg['FromUserName'])
        LOG.info(msg)
    except Exception:
        LOG.record_except()


@itchat.msg_register(FRIENDS)
def new_friend(msg):
    """friend"""
    try:
        time.sleep(randint(2, 5))
        itchat.add_friend(msg['RecommendInfo']['UserName'], status=3)
        time.sleep(randint(1, 3))
        itchat.send_msg(msg='欢迎添加三星电气经验共享平台助手。\n您可以使用办公室网络访问 http://10.9.52.233 进入平台（推荐使用Chrome或Firefox浏览器，请勿使用IE）。\n经验共享平台，让我们每天都能经验+1！',\
                            toUserName=msg['RecommendInfo']['UserName'])
        LOG.info(msg)
    except Exception:
        LOG.record_except()



def main():
    """main"""
    itchat.auto_login(hotReload=True)
    itchat.run()


if __name__ == "__main__":
    main()

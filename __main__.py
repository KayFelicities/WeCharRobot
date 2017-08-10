"""main"""
import time
from random import randint
from pprint import pprint
import itchat
from itchat.content import TEXT, FRIENDS


@itchat.msg_register(TEXT)
def text_reply(msg):
    """text"""
    pprint(msg)
    time.sleep(randint(1, 3))
    itchat.send_msg(msg='平台网址：http://10.9.52.233 。经验共享平台，让我们每天都能经验+1！', toUserName=msg['FromUserName'])


@itchat.msg_register(FRIENDS)
def new_friend(msg):
    """friend"""
    pprint(msg)
    time.sleep(randint(2, 5))
    itchat.add_friend(msg['RecommendInfo']['UserName'], status=3)
    time.sleep(randint(1, 3))
    itchat.send_msg(msg='欢迎添加三星电气经验共享平台助手。您可以使用办公室网络访问 http://10.9.52.233 进入平台（推荐使用Chrome或Firefox浏览器，请勿使用IE）。经验共享平台，让我们每天都能经验+1！',\
                        toUserName=msg['RecommendInfo']['UserName'])



def main():
    """main"""
    itchat.auto_login(hotReload=True)
    itchat.run()


if __name__ == "__main__":
    main()

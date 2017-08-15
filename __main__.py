# coding='utf-8'
"""main"""
from pprint import pprint
import traceback
import time
from random import uniform
import itchat
from itchat.content import TEXT, FRIENDS

import config
from log import Logger


LOG = Logger('main', config.ERROR_LOG)

NEW_FRIEND_REPLY = ('您好，欢迎加入三星电气经验共享平台！\n'
                    '在这里您可以查阅最新最全的用电产品经验，可以感受最真最纯的企业文化熏陶，可以发现多维立体的个人成长历程!\n'
                    '在这里，您既是观光浏览者，又是网站建设者，这是一个共享的时代，我们为您搭建了一个共享的平台，分享、交流、互动，这里将成为技术人员思维碰撞的殿堂，每天多一些分享，多一些互动，让您每天经验+1！\n'
                    '23号前为文章评论、点赞、上传经验，参与千元红包共享活动（仅用电产品中心）。\n'
                    '详情请访问网站 http://10.9.52.233 （仅公司网络可访问，请使用Chrome浏览器）')

TEXT_REPLY = ('经验共享平台，让我们每天都能经验+1！\n'
                '网址 http://10.9.52.233 (仅公司网络可访问，请使用Chrome浏览器)')

def get_right_str(text):
    """encode then decode"""
    return text.encode('gbk', 'ignore').decode('gbk', 'ignore')

@itchat.msg_register(TEXT)
def text_reply(msg):
    """text"""
    try:
        if msg['User']['NickName'] == 'Kay' and msg['Content'].find('我们#') == 0:
            send_text = u'%s，%s'
            friend_list = itchat.get_friends(update=True)[1:]
            for friend in friend_list:
                if (friend.get('NickName', '') and friend.get('NickName', '') != '朋友推荐消息'):
                    itchat.send(send_text % (get_right_str(friend['DisplayName']) or get_right_str(friend['NickName']), msg['Content'][4:]), friend['UserName'])
                time.sleep(uniform(1, 2))
            itchat.send_msg(msg='done', toUserName=msg['FromUserName'])
        else:
            time.sleep(uniform(1, 3))
            itchat.send_msg(msg='欢迎您，%s！\n%s'%(get_right_str(msg['User']['NickName']), TEXT_REPLY),\
                                toUserName=msg['FromUserName'])
            LOG.info(msg)
    except Exception:
        LOG.record_except()


@itchat.msg_register(FRIENDS)
def new_friend(msg):
    """friend"""
    try:
        time.sleep(uniform(1, 3))
        itchat.add_friend(msg['RecommendInfo']['UserName'], status=3)
        time.sleep(uniform(1, 3))
        itchat.send_msg(msg='%s，%s'%(get_right_str(msg['RecommendInfo']['NickName']), NEW_FRIEND_REPLY),\
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

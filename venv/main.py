# coding=utf8
import itchat
# tuling plugin can be get here:
# https://github.com/littlecodersh/EasierLife/tree/master/Plugins/Tuling
from tuling import get_response


# itchat.send('Hello, filehelper', toUserName='filehelper')
@itchat.msg_register('Text')
def text_reply(msg):
    if u'作者' in msg['Text'] or u'主人' in msg['Text']:
        return u'你可以在这里了解他：https://github.com/littlecodersh'
    elif u'源代码' in msg['Text'] or u'获取文件' in msg['Text']:
        itchat.send('@fil@main.py', msg['FromUserName'])
        return u'这就是现在机器人后台的代码，是不是很简单呢？'
    elif u'获取图片' in msg['Text']:
        itchat.send('@img@applaud.gif', msg['FromUserName']) # there should be a picture
    else:
        return get_response(msg['Text']) or u'收到：' + msg['Text']

itchat.auto_login()
itchat.run()
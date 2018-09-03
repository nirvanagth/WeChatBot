# coding=utf8
import itchat
# tuling plugin can be get here:
# https://github.com/littlecodersh/EasierLife/tree/master/Plugins/Tuling
from tuling import tuling_response
import requests
import random
import os


replied = []

# itchat.send('Hello, filehelper', toUserName='filehelper')
@itchat.msg_register('Text')
def text_reply(msg):
    if '吃啥' in msg['Text']:
        return 'yelp_response()'
    elif '生日' in msg['Text']:
        itchat.send('谢谢呀，感动感谢！', msg['FromUserName'])
    elif '牛逼' in msg['Text'] or '厉害' in msg['Text']:
        itchat.send('哈哈哈哈哈', msg['FromUserName'])
        path = './img/guitar.gif'
        itchat.send_image(path, msg['FromUserName'])
    elif '新年' in msg['Text'] and msg['FromUserName'] not in replied:
        sendHappyNewYear(msg)
    elif msg['FromUserName'] not in replied:
        path = './img/listening.gif'
        itchat.send(u'天豪大概在休息呢，你的消息已经收到啦，稍后会回复哒', msg['FromUserName'])
        itchat.send_image(path, msg['FromUserName'])
        replied.append(msg['FromUserName'])
    else:
        itchat.send(tuling_response(msg['Text']), msg['FromUserName'])

# filename has to be english
@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def other_reply(msg):

    # path = './img/stop.gif'
    # itchat.send_image(path, msg['FromUserName'])
    # return ({'Picture': u'图片', 'Recording': u'录音',
    #          'Attachment': u'附件', 'Video': u'视频', }.get(msg['Type']) +
    #         u'已下载到本地')
    sendRandomEmoji(msg)
    # if msg['FromUserName'] not in replied:
    #     sendHappyNewYear(msg)

def sendHappyNewYear(msg):
    global replied
    friend = itchat.search_friends(userName=msg['FromUserName'])
    print(friend)
    itchat.send((friend['RemarkName'] + '，感动，感谢！' + getRandomGreeting()), msg['FromUserName'])
    replied.append(msg['FromUserName'])


def getRandomGreeting():
    response = requests.get("http://www.xjihe.com/api/life/greetings?festival=新年&page=2",
                            headers={'apiKey': 'sQS2ylErlfm9Ao2oNPqw6TqMYbJjbs4g'})
    results = response.json()['result']
    greeting = results[random.randrange(len(results))]['words']
    return greeting

def sendRandomEmoji(msg):
    fileName = ""
    img_path = os.path.abspath('.') + os.path.sep + "img"
    while not os.path.isfile(fileName):
        fileName = img_path + os.path.sep + random.choice(os.listdir('./img'))

    itchat.send_image(fileName, msg['FromUserName'])



itchat.auto_login(hotReload=True)
itchat.run()
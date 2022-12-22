from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from linebot.models import TextSendMessage, ImageSendMessage

#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========
#======讓heroku不會睡著======
import threading 
import requests
def wake_up_heroku():
    while 1==1:
        url = ' https://fbiccline-n133.onrender.com/' + 'heroku_wake_up'
        res = requests.get(url)
        if res.status_code==200:
            print('喚醒heroku成功')
        else:
            print('喚醒失敗')
        time.sleep(14*60)

threading.Thread(target=wake_up_heroku).start()
#======讓heroku不會睡著======

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('CO2OtMpM56swuN17zBq1WOFkA3jNynbNkX/PGfJ/v3ZWEzTVPXLPKHjW8B1gGn7vTayhm/drghUMP9Czy38+6awKLDZDjoKieIOZ8dFkcZBaFbK9GOaL8Odk1MYhcwOTRIITeN46ajTMGCgg0OZ/uAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('9c3008c553f0ff6e9e2fc1c524a70311')


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header valuehe
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '中心服務' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '我要報名' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '管理委員會' in msg:
        message = buttons_message2()
        line_bot_api.reply_message(event.reply_token, message)
    elif '招募員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '公設管理' in msg:
        message = Carousel_Template1()
        line_bot_api.reply_message(event.reply_token, message)
    elif '生活公約' in msg:
        message = Carousel_Template2()
        line_bot_api.reply_message(event.reply_token, message)
    elif '管委會成員' in msg:
        message = Carousel_Template3()
        line_bot_api.reply_message(event.reply_token, message)
    elif '陸岸一般' in msg:
        message = Carousel_Template4()
        line_bot_api.reply_message(event.reply_token, message)
    elif '海軍影片' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    elif 'I郵箱' in msg:  
        message =[ 
            TextSendMessage(
                text="I郵箱簡易操作影片", 
            ),
            VideoSendMessage(
                original_content_url='https://dai.ly/k4hfzDg5j8BDWnyBL42', 
                preview_image_url='https://upload.cc/i1/2022/12/20/5Y3GqJ.jpg'
            ),
            VideoSendMessage(
                original_content_url='https://dai.ly/k28wNgeDJbxtoGyBL3S', 
                preview_image_url='https://upload.cc/i1/2022/12/20/lEwKBU.jpg'
            ),
            VideoSendMessage(
                original_content_url='https://dai.ly/k4Qtx7reGQQIj1yBL4e', 
                preview_image_url='https://upload.cc/i1/2022/12/20/J4ZnHm.jpg'
            )
        ]
        line_bot_api.reply_message(event.reply_token, message)    
          
    #艦隊簡介    
#    elif '%124' in msg:  
#        message = TextSendMessage(text="⚓ 海軍一二四艦隊 ⚓\n區域：南部地區\n主力軍艦：\n🇹🇼康定級飛彈巡防艦🇹🇼\n依海軍「光華2號計畫」，由法國海軍造艦局承造，原型為法國海軍拉法葉級巡防艦，為中華民國海軍的一級艦，主要執行台灣海峽周遭防空、反潛、護航、反封鎖及聯合水面截擊作戰。85年5月第一艘「康定艦」返國。該型艦滿載排水量為3,680噸，以四部柴油主機推動，最高航速25節。\n📃命名方式📃\n康定級巡防艦以中華民國西康省省會康定市命名，之後艦艇的命名均以中華民國各省會來命名。\n-⚓同級艦(舷號)⚓-\n康定軍艦(PFG-1202)\n西寧軍艦(PFG-1203)\n昆明軍艦(PFG-1205)\n迪化軍艦(PFG-1206)\n武昌軍艦(PFG-1207)\n承德軍艦(PFG-1208)\n💰薪資待遇💰\n戰鬥加給：5000元\n海勤加給(士兵)：4000元\n海勤加給(士官)：17500元\n💎各階待遇💎\n士兵起薪：44320元\n士官起薪：63950元\n軍官起薪：73060元" )
#        line_bot_api.reply_message(event.reply_token, message)   
    #其他功能    
#    elif '海軍小百科預告'in msg:
#        message = VideoSendMessage(original_content_url='https://i.imgur.com/ds1LiqC.mp4', preview_image_url='https://i.imgur.com/upYB4x9.jpg')
#        line_bot_api.reply_message(event.reply_token, message)
#    elif '認識海軍'in msg:
#        message = buttons_message2()
#       line_bot_api.reply_message(event.reply_token, message)    
    elif '小編'in msg:
        message = ImageSendMessage(original_content_url="https://i.imgur.com/evPGRYz.jpg", preview_image_url="https://i.imgur.com/evPGRYz.jpg")
        line_bot_api.reply_message(event.reply_token, message)
#  else:
#  #      message = buttons_message1()
 #       line_bot_api.reply_message(event.reply_token, message)


@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



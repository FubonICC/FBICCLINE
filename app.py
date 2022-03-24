from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


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
        url = ' https://navy-dw.herokuapp.com/' + 'heroku_wake_up'
        res = requests.get(url)
        if res.status_code==200:
            print('喚醒heroku成功')
        else:
            print('喚醒失敗')
        time.sleep(28*60)

threading.Thread(target=wake_up_heroku).start()
#======讓heroku不會睡著======

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('VZZP9zRYy4OYEUW/6Myjr7XlxJuldLu/PX4d7k2gQ2PK6pDqSjbOklZLw0iF9qM2x4R/GIhwpp6s1Dc7nmXnPGI6AHwyMGY6LytHWeUmLh95bul74HVSPrvuNDsqoj8T9/OzYyVhTE2j2SVlDSKNfAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('03bec986bf0c59bae80cdcb373b6fde4')


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
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
    if '最新合作廠商' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '我要報名' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊會員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '海軍艦隊' in msg:
        message = Carousel_Template1()
        line_bot_api.reply_message(event.reply_token, message)
    elif '海軍陸戰隊' in msg:
        message = Carousel_Template2()
        line_bot_api.reply_message(event.reply_token, message)
    elif '陸岸' in msg:
        message = Carousel_Template3()
        line_bot_api.reply_message(event.reply_token, message)
    elif '海軍影片' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    elif '左營軍港' in msg:
        message = LocationSendMessage(
            title="左營軍港",
            address="左營海軍基地",
            latitude="22.6931019",
            longitude="120.2607194"
         )
        line_bot_api.reply_message(event.reply_token, message)
    elif '蘇澳軍港' in msg:
        message = LocationSendMessage(
            title="蘇澳軍港",
            address="中正軍港",
            latitude="24.6018080",
            longitude="121.8792230"
         )
        line_bot_api.reply_message(event.reply_token, message)
    elif '基隆軍港' in msg:
        message = LocationSendMessage(
            title="基隆軍港",
            address="威海營區",
            latitude="25.1363810",
            longitude="121.7471660"
         )
        line_bot_api.reply_message(event.reply_token, message)
    elif '馬公軍港' in msg:
        message = LocationSendMessage(
            title="馬公基地",
            address="馬公港",
            latitude="23.5541179",
            longitude="119.5635929"
         )
        line_bot_api.reply_message(event.reply_token, message)
    elif '薪水' in msg:    
        message = TextSendMessage(text="★111年度國軍基本薪資結構★\n-----士兵-----\n二兵（1級）\n本俸加給：10130\n專業加給：15190\n志願加給：10000\n合計底薪：35320元\n \n一兵（1級）\n本俸加給：10910\n專業加給：16130\n志願加給：10000\n合計底薪：37040元\n  \n上兵（1級）\n本俸加給：11690\n專業加給：17080\n志願加給：10000\n合計底薪：38770元\n  \n-----士官-----\n下士（1級）\n本俸加給：12470\n專業加給：18980\n志願加給：10000\n合計底薪：41450元\n \n中士（1級）\n本俸加給：16210\n專業加給：19050\n志願加給：10000\n合計底薪：45260元\n \n上士（1級）\n本俸加給：19780\n專業加給：19110\n志願加給：10000\n合計底薪：48890元\n \n三等士官長（1級）\n本俸加給：21200\n專業加給：20260\n志願加給：10000\n合計底薪：51460元\n \n二等士官長（1級）\n本俸加給：23350\n專業加給：22280\n志願加給：10000\n合計底薪：55630元\n \n一等士官長（1級）\n本俸加給：26920\n專業加給：23270\n志願加給：10000\n合計底薪：60190元\n \n-----軍官-----\n少尉（1級）\n本俸加給：21200\n專業加給：19360\n志願加給：10000\n合計底薪：50560元\n \n中尉（1級）\n本俸加給：23350\n專業加給：20260\n志願加給：10000\n合計底薪：53610元\n \n上尉（1級）\n本俸加給：26920\n專業加給：22280\n志願加給：10000\n合計底薪：59200元\n \n\n少校（1級）\n本俸加給：30490\n專業加給：23270\n志願加給：10000\n合計底薪：63760元" )
        line_bot_api.reply_message(event.reply_token, message)   
    elif '%124'in msg:     
        message = TextSendMessage(text="⚓ 海軍一二四艦隊 ⚓\n駐地：左營軍港\n主力軍艦：🇹🇼康定級飛彈巡防艦🇹🇼\n依海軍「光華2號計畫」，由法國海軍造艦局承造，85年5月第一艘「康定艦」返國。該型艦滿載排水量為3,680噸，以四部柴油主機推動，最高航速25節。\n-⚓同級艦(舷號)⚓-\n康定軍艦(PFG-1202)\n西寧軍艦(PFG-1203)\n昆明軍艦(PFG-1205)\n迪化軍艦(PFG-1206)\n武昌軍艦(PFG-1207)\n承德軍艦(PFG-1208)\n💰薪資待遇💰\n戰鬥加給：5000元\n海勤加給(士兵)：4000元\n海勤加給(士官)：17500元\n💎各階待遇💎\n士兵起薪：44320元\n士官起薪：63950元\n軍官起薪：73060元" )
        line_bot_api.reply_message(event.reply_token, message)   
    else:
        message = TextSendMessage(text="你說的是不是:" + event.message.text)
        line_bot_api.reply_message(event.reply_token, message)


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



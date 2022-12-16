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
        url = ' https://fbiccapp.herokuapp.com/' + 'heroku_wake_up'
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
    elif '招募員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '海軍艦隊' in msg:
        message = Carousel_Template1()
        line_bot_api.reply_message(event.reply_token, message)
    elif '海軍陸戰隊' in msg:
        message = Carousel_Template2()
        line_bot_api.reply_message(event.reply_token, message)
    elif '陸岸作戰' in msg:
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
 #   elif '海軍左營軍港' in msg:
        message = LocationSendMessage(
            title="左營軍港",
            address="左營海軍基地",
            latitude="22.6931019",
            longitude="120.2607194"
         )
        line_bot_api.reply_message(event.reply_token, message)
 #   elif '海軍蘇澳軍港' in msg:
        message = LocationSendMessage(
            title="蘇澳軍港",
            address="中正軍港",
            latitude="24.6018080",
            longitude="121.8792230"
         )
        line_bot_api.reply_message(event.reply_token, message)
#    elif '海軍基隆軍港' in msg:
        message = LocationSendMessage(
            title="基隆軍港",
            address="威海營區",
            latitude="25.1363810",
            longitude="121.7471660"
         )
        line_bot_api.reply_message(event.reply_token, message)
#    elif '海軍馬公軍港' in msg:
        message = LocationSendMessage(
            title="馬公基地",
            address="馬公港",
            latitude="23.5541179",
            longitude="119.5635929"
         )
        line_bot_api.reply_message(event.reply_token, message)#
    elif '薪水' in msg:    
        message = TextSendMessage(text="★111年度國軍基本薪資結構★\n-----士兵-----\n二兵（1級）\n本俸加給：10130\n專業加給：15190\n志願加給：10000\n合計底薪：35320元\n \n一兵（1級）\n本俸加給：10910\n專業加給：16130\n志願加給：10000\n合計底薪：37040元\n  \n上兵（1級）\n本俸加給：11690\n專業加給：17080\n志願加給：10000\n合計底薪：38770元\n  \n-----士官-----\n下士（1級）\n本俸加給：12470\n專業加給：18980\n志願加給：10000\n合計底薪：41450元\n \n中士（1級）\n本俸加給：16210\n專業加給：19050\n志願加給：10000\n合計底薪：45260元\n \n上士（1級）\n本俸加給：19780\n專業加給：19110\n志願加給：10000\n合計底薪：48890元\n \n三等士官長（1級）\n本俸加給：21200\n專業加給：20260\n志願加給：10000\n合計底薪：51460元\n \n二等士官長（1級）\n本俸加給：23350\n專業加給：22280\n志願加給：10000\n合計底薪：55630元\n \n一等士官長（1級）\n本俸加給：26920\n專業加給：23270\n志願加給：10000\n合計底薪：60190元\n \n-----軍官-----\n少尉（1級）\n本俸加給：21200\n專業加給：19360\n志願加給：10000\n合計底薪：50560元\n \n中尉（1級）\n本俸加給：23350\n專業加給：20260\n志願加給：10000\n合計底薪：53610元\n \n上尉（1級）\n本俸加給：26920\n專業加給：22280\n志願加給：10000\n合計底薪：59200元\n \n\n少校（1級）\n本俸加給：30490\n專業加給：23270\n志願加給：10000\n合計底薪：63760元" )
        line_bot_api.reply_message(event.reply_token, message)   
    elif '體能鑑測' in msg:    
        message = TextSendMessage(text="為提倡多元運動，原「基本體能」修調為「國軍體能多元訓練」，不再區分專長職類適用多元選項，改全體人員適用，於112年起實施。\n\n🟥年齡層\n🔷青年期：19-29歲\n🔷壯年期：30-44歲\n🔷中年期：45-59歲\n\n🟥測驗項目(每個大項選一小項)\n🔷上肢肌群\n🔺伏地挺身\n▪️青：男40下、女21下\n▪️壯：男30下、女15下\n▪️中：男20下、女8下\n\n🔺男子引體向上/女子曲臂懸垂\n▪️青：男5下、女20秒\n▪️壯：男3下、女14秒\n▪️中：男2下、女8秒\n\n🔺壺鈴平舉(10公斤)\n▪️青：男40下、女30下\n▪️壯：男30下、女20下\n▪️中：男20下、女10下\n\n🔷腹部核心肌群\n🔺仰臥起坐\n▪️青：男42下、女31下\n▪️壯：男35下、女23下\n▪️中：男20下、女16下\n\n🔺平板撐體\n▪️青：男85秒、女85秒\n▪️壯：男70秒、女70秒\n▪️中：男70秒、女70秒\n\n🔺仰臥捲腹\n▪️青：男31下、女27下\n▪️壯：男24下、女21下\n▪️中：男20下、女17下\n\n🔷下肢肌力\n🔺三千公尺跑步\n▪️青：男14”45、女17”35\n▪️壯：男16”30、女19”00\n▪️中：男18”00、女21”00\n\n🔺五分鐘跳繩\n▪️青：男530下、女430下\n▪️壯：男499下、女399下\n▪️中：男462下、女362下\n\n🔺五公里健走\n▪️青：男40”20、女44”20\n▪️壯：男41”40、女45”50\n▪️中：男45”00、女49”00\n\n🔺八百公尺遊走\n▪️青：男25”30、女28”30\n▪️壯：男27”00、女30”00\n▪️中：男28”30、女31”30\n\n🔺二十公尺漸進式折返跑\n▪️青：男50趟、女40趟\n▪️壯：男35趟、女25趟\n▪️中：男25趟、女15趟\n" )
        line_bot_api.reply_message(event.reply_token, message)  
    elif '體測' in msg:    
        message = TextSendMessage(text="為提倡多元運動，原「基本體能」修調為「國軍體能多元訓練」，不再區分專長職類適用多元選項，改全體人員適用，於112年起實施。\n\n🟥年齡層\n🔷青年期：19-29歲\n🔷壯年期：30-44歲\n🔷中年期：45-59歲\n\n🟥測驗項目(每個大項選一小項)\n🔷上肢肌群\n🔺伏地挺身\n▪️青：男40下、女21下\n▪️壯：男30下、女15下\n▪️中：男20下、女8下\n\n🔺男子引體向上/女子曲臂懸垂\n▪️青：男5下、女20秒\n▪️壯：男3下、女14秒\n▪️中：男2下、女8秒\n\n🔺壺鈴平舉(10公斤)\n▪️青：男40下、女30下\n▪️壯：男30下、女20下\n▪️中：男20下、女10下\n\n🔷腹部核心肌群\n🔺仰臥起坐\n▪️青：男42下、女31下\n▪️壯：男35下、女23下\n▪️中：男20下、女16下\n\n🔺平板撐體\n▪️青：男85秒、女85秒\n▪️壯：男70秒、女70秒\n▪️中：男70秒、女70秒\n\n🔺仰臥捲腹\n▪️青：男31下、女27下\n▪️壯：男24下、女21下\n▪️中：男20下、女17下\n\n🔷下肢肌力\n🔺三千公尺跑步\n▪️青：男14”45、女17”35\n▪️壯：男16”30、女19”00\n▪️中：男18”00、女21”00\n\n🔺五分鐘跳繩\n▪️青：男530下、女430下\n▪️壯：男499下、女399下\n▪️中：男462下、女362下\n\n🔺五公里健走\n▪️青：男40”20、女44”20\n▪️壯：男41”40、女45”50\n▪️中：男45”00、女49”00\n\n🔺八百公尺遊走\n▪️青：男25”30、女28”30\n▪️壯：男27”00、女30”00\n▪️中：男28”30、女31”30\n\n🔺二十公尺漸進式折返跑\n▪️青：男50趟、女40趟\n▪️壯：男35趟、女25趟\n▪️中：男25趟、女15趟\n" )
        line_bot_api.reply_message(event.reply_token, message)           
    #艦隊簡介    
    elif '%124' in msg:  
        message = TextSendMessage(text="⚓ 海軍一二四艦隊 ⚓\n區域：南部地區\n主力軍艦：\n🇹🇼康定級飛彈巡防艦🇹🇼\n依海軍「光華2號計畫」，由法國海軍造艦局承造，原型為法國海軍拉法葉級巡防艦，為中華民國海軍的一級艦，主要執行台灣海峽周遭防空、反潛、護航、反封鎖及聯合水面截擊作戰。85年5月第一艘「康定艦」返國。該型艦滿載排水量為3,680噸，以四部柴油主機推動，最高航速25節。\n📃命名方式📃\n康定級巡防艦以中華民國西康省省會康定市命名，之後艦艇的命名均以中華民國各省會來命名。\n-⚓同級艦(舷號)⚓-\n康定軍艦(PFG-1202)\n西寧軍艦(PFG-1203)\n昆明軍艦(PFG-1205)\n迪化軍艦(PFG-1206)\n武昌軍艦(PFG-1207)\n承德軍艦(PFG-1208)\n💰薪資待遇💰\n戰鬥加給：5000元\n海勤加給(士兵)：4000元\n海勤加給(士官)：17500元\n💎各階待遇💎\n士兵起薪：44320元\n士官起薪：63950元\n軍官起薪：73060元" )
        line_bot_api.reply_message(event.reply_token, message)   
    #其他功能    
    elif '海軍小百科預告'in msg:
        message = VideoSendMessage(original_content_url='https://i.imgur.com/ds1LiqC.mp4', preview_image_url='https://i.imgur.com/upYB4x9.jpg')
        line_bot_api.reply_message(event.reply_token, message)
    elif '認識海軍'in msg:
        message = buttons_message2()
        line_bot_api.reply_message(event.reply_token, message)
    elif '海軍官網'in msg:
        message = buttons_message3()
        line_bot_api.reply_message(event.reply_token, message)
    elif '海軍簡報'in msg:
        message = buttons_message4()
        line_bot_api.reply_message(event.reply_token, message)

    elif '112梯次'in msg:
        message = ImageSendMessage(original_content_url="https://i.imgur.com/wzszzFx.jpg", preview_image_url="https://i.imgur.com/wzszzFx.jpg")
        line_bot_api.reply_message(event.reply_token, message)        
    elif '小編'in msg:
        message = ImageSendMessage(original_content_url="https://i.imgur.com/evPGRYz.jpg", preview_image_url="https://i.imgur.com/evPGRYz.jpg")
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = buttons_message1()
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



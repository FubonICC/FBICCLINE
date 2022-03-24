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
    elif '%124' or '一二四'in msg:     
        message = TextSendMessage(text="⚓ 海軍一二四艦隊 ⚓\n駐地：左營軍港\n主力軍艦：\n🇹🇼康定級飛彈巡防艦🇹🇼\n依海軍「光華2號計畫」，由法國海軍造艦局承造，85年5月第一艘「康定艦」返國。該型艦滿載排水量為3,680噸，以四部柴油主機推動，最高航速25節。\n-⚓同級艦(舷號)⚓-\n康定軍艦(PFG-1202)\n西寧軍艦(PFG-1203)\n昆明軍艦(PFG-1205)\n迪化軍艦(PFG-1206)\n武昌軍艦(PFG-1207)\n承德軍艦(PFG-1208)\n💰薪資待遇💰\n戰鬥加給：5000元\n海勤加給(士兵)：4000元\n海勤加給(士官)：17500元\n💎各階待遇💎\n士兵起薪：44320元\n士官起薪：63950元\n軍官起薪：73060元" )
        line_bot_api.reply_message(event.reply_token, message)   
    elif '%131'in msg:     
        message = TextSendMessage(text="⚓ 海軍一三一艦隊 ⚓\n駐地：基隆軍港\n主力軍艦：\n🇹🇼錦江級巡邏艦🇹🇼\n中華民國海軍與聯合船舶設計發展中心參考海關購自荷蘭的緝私艦（謀星艦、福星艦，現已移交海巡署使用）的設計，並由國內聯合造船廠（已被中信造船購併）建造而成的500噸級巡邏艦，用於近海巡邏之用。\n📃命名方式📃\n錦江級艦後依成軍時間排列計有淡江（淡水河）、新江（新店溪）、鳳江（鳳山溪）、曾江（曾文溪）、高江（高屏溪）、金江、湘江、資江、鄱江、昌江、珠江合計11艘，前六艦之命名係以本島各大名川為主，鄱江、昌江、珠江等後三艦之命名係源於海軍前期汰除之戰功艦，以資紀念，並作為後續艦上官兵之期許，繼志成烈，惕勵奮發，已捍衛我海疆，同級艦型共計12艘。\n-⚓同級艦(舷號)⚓-\n錦江艦(PGG-603)(已除役)\n淡江艦(PGG-605)\n新江艦(PGG-606)\n鳳江艦(PGG-607)\n曾江艦(PGG-608)\n高江艦(PGG-609)\n金江艦(PGG-610)\n湘江艦(PGG-611)\n資江艦(PGG-612)\n鄱江艦(PGG-614)\n昌江艦(PGG-615)\n珠江艦(PGG-617)\n \n \n🇹🇼沱江級巡邏艦🇹🇼\n中華民國海軍的匿蹤雙船體飛彈巡邏艦，可與光華六號飛彈快艇混編執行反艦與反船團任務，也因匿蹤、快速、火力強等特性而被譽為「航母殺手」。\n📃命名方式📃\n民國47年8月23日起共軍日以繼夜砲轟金門，敵艦並猝襲料羅灣，在9月2日的海戰中， 我海軍「維源」、「柳江」、 「沱江」、「美頌」四艦擊沉敵各式艦艇12艘，其中以沱江軍艦擊沉中共艦艇5艘、重傷2艘，戰果最為輝煌，並獲頒海軍第一面榮譽虎旗。\n為紀念「九二海戰」中重創敵艦之沱江軍艦，民國104年4月3日由國人設計建造編號618之「高效能原型艦」，命名為「沱江軍艦」正式成軍，期能承續沱江軍艦光榮傳統，擔負起護衛海疆的重責大任，再創沱江的光榮史頁。\n-⚓同級艦(舷號)⚓-\n沱江艦(PGG-618)\n  \n  \n🇹🇼塔江級巡邏艦🇹🇼\n中華民國海軍沱江級巡邏艦二號艦，簡稱塔江艦、塔江軍艦，為最初中華民國海軍自2014年開始規劃之十二項造艦計畫之一，中華民國海軍稱此計劃為「高效能艦艇後續量產（承海計劃）」，由於與首艦沱江號頗有差異，因此也有將塔江艦為首艦另成一級成為「塔江級巡邏艦」\n📃命名方式📃\n艦名出自台東縣塔瓦溪，取「塔」字搭配中華民國海軍巡邏艦命名模式「江」字而成，亦為至塔江號為止歷來所使用長度最短之河川，中華民國海軍司令部說明，該溪流屬排灣族生活領域，該族人天性具有不畏艱難，秉持著驍勇善戰的精神，足堪本艦官兵效法；另「塔」字象徴此艦擔任海上堡壘，保衛民主自由的中華民國，亦代表國艦國造工作篳路藍縷，積沙成塔，方能建造符合國人期待的優異艦艇。\n-⚓同級艦(舷號)⚓-\n塔江艦(PGG-619)\n  \n \n🇹🇼光華六號飛彈快艇🇹🇼\n簡稱光六，為台灣國際造船（CSBC，簡稱為台船，2007年前名為中國造船公司）為中華民國海軍製造的飛彈快艇，隸屬海軍一三一艦隊，屬於近岸作戰打擊兵力。\n📃命名方式📃  \n 與海鷗飛彈快艇相同，光六艇也僅以編號區別而無命名，共計31艘。\n-⚓同級艦舷號⚓-\nFACG-60~66\nFACG-68~75\nFACG-77~84\nFACG-86~93\n \n💰薪資待遇💰\n戰鬥加給：5000元\n海勤加給(士兵)：4000元\n海勤加給(士官)：17500元\n💎各階待遇💎\n士兵起薪：44320元\n士官起薪：63950元\n軍官起薪：73060元" )
        line_bot_api.reply_message(event.reply_token, message)  
    elif '%146'in msg:     
        message = TextSendMessage(text="⚓ 海軍一四六艦隊 ⚓\n駐地：馬公軍港\n主力軍艦：\n🇹🇼成功級巡防艦🇹🇼\n成功級巡防艦是海軍現役巡防艦，為美國海軍派里級巡防艦的修改型，具有優越靈活之機動力及精良準確之系統，結合現代化之武器裝備，滿足台澎防衛作戰「縱深淺、預警短、決戰快」的特性需求，達到「掌握機先、早期預警、快速反應、指揮作戰的整備目標」，達成鞏固海軍第一線防務為目標。\n📃命名方式📃\n成功級10艘同型艦以中國古代戰將來命名。\n-⚓同級艦(舷號)⚓-\n成功軍艦(PFG-1101)\n鄭和軍艦(PFG-1103)\n繼光軍艦(PFG-1105)\n岳飛軍艦(PFG-1106)\n子儀軍艦(PFG-1107)\n班超軍艦(PFG-1108)\n張騫軍艦(PFG-1109)\n田單軍艦(PFG-1110)\n銘傳軍艦(PFG-1112)\n逢甲軍艦(PFG-1115)\n💰薪資待遇💰\n戰鬥加給：5000元\n海勤加給(士兵)：4000元\n海勤加給(士官)：17500元\n離島加給：7700元\n💎各階待遇💎\n士兵起薪：52020元\n士官起薪：71650元\n軍官起薪：80760元" )
        line_bot_api.reply_message(event.reply_token, message)   
    elif '%168'in msg:     
        message = TextSendMessage(text="⚓ 海軍一六八艦隊 ⚓\n駐地：蘇澳軍港\n主力軍艦：\n🇹🇼紀德級驅逐艦🇹🇼\n原為美國海軍紀德級驅逐艦（Kidd class），這是種以史普魯恩斯級（Spruance-class）驅逐艦的船身為基礎，但配置不同武裝與電子設備的改良版本。平時基隆級將擔任重要海域偵搜巡邏任務，並擴大其監偵範圍以增加中華民國國軍預警反應時間；戰時主要擔任由不同作戰艦艇組成海軍作戰艦隊旗艦，扼控重要海域阻敵進犯，並可為陸基作戰中心與戰管中心遭受損毀時的備援防空指揮管制任務，進行聯合制空、制海作戰。\n📃命名方式📃\n最初四艘軍艦的命名原計劃沿用本艦美軍艦名的譯名為名，再衍生為「德字號」而分別為「紀德」、「明德」、「同德」、「武德」，以彰顯海軍「紀律嚴明，同揚武德」之軍風。但2005年立法院做成決議，要求今後艦名必須以台灣的人名或地名命名，故成軍時各艦改成以台灣四大軍港命名、首兩艘艦、前美軍DDG-995及DDG-994，於2005年12月抵達臺灣，分別命名為「基隆」（DDG-1801）與「蘇澳」(DDG-1802)。前美軍DDG-993及DDG-996艦則於2006年10月25日抵達臺灣，被命名為「左營」（DDG-1803）與「馬公」（DDG-1805）。依據命名軍艦級別的傳統，中華民國海軍對其的正式命名為基隆級驅逐艦。\n-⚓同級艦(舷號)⚓-\n基隆軍艦(DDG-1801)\n蘇澳軍艦(DDG-1802)\n左營軍艦(DDG-1803)\n馬公軍艦(DDG-1805)\n💰薪資待遇💰\n戰鬥加給：5000元\n海勤加給(士兵)：4000元\n海勤加給(士官)：17500元\n💎各階待遇💎\n士兵起薪：44320元\n士官起薪：63950元\n軍官起薪：73060元\n \n \n🇹🇼濟陽級巡防艦🇹🇼\n為中華民國海軍在1990年代初向美國海軍租借之諾克斯級巡防艦經過後續改良而成的艦型，本級艦的設計以遠洋反潛能力著稱，在中華民國海軍服役以來主要負擔台灣東北部至東部海域的巡防任務，多次偵測行經台灣東部海域之各國潛艦。\n📃命名方式📃\n依據地名命名法，8艘濟陽級巡防艦分別命名為濟陽(舷號932)、鳳陽(舷號933)、汾陽(舷號934)、蘭陽(舷號935)、海陽(舷號936)、淮陽(舷號937)、宜陽(舷號938)、寧陽(舷號939)。\n-⚓同級艦(舷號)⚓-\n濟陽軍艦(FFG-932)(已除役)\n鳳陽軍艦(FFG-933)\n汾陽軍艦(FFG-934)\n蘭陽軍艦(FFG-935)\n海陽軍艦(FFG-936)(已除役)\n淮陽軍艦(FFG-937)\n寧陽軍艦(FFG-938)\n宜陽軍艦(FFG-939)\n💰薪資待遇💰\n戰鬥加給：5000元\n海勤加給(艙面士兵)：4000元\n海勤加給(艙底士兵)：10000元\n海勤加給(士官)：17500元\n💎各階待遇💎\n艙面士兵起薪：44320元\n艙底士兵起薪：50320\n士官起薪：63950元\n軍官起薪：73060元" )
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



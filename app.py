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
    if '中心服務' in msg:
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
    #艦隊簡介    
    elif '%124' in msg:  
        message = TextSendMessage(text="⚓ 海軍一二四艦隊 ⚓\n駐地：左營軍港\n主力軍艦：\n🇹🇼康定級飛彈巡防艦🇹🇼\n依海軍「光華2號計畫」，由法國海軍造艦局承造，85年5月第一艘「康定艦」返國。該型艦滿載排水量為3,680噸，以四部柴油主機推動，最高航速25節。\n-⚓同級艦(舷號)⚓-\n康定軍艦(PFG-1202)\n西寧軍艦(PFG-1203)\n昆明軍艦(PFG-1205)\n迪化軍艦(PFG-1206)\n武昌軍艦(PFG-1207)\n承德軍艦(PFG-1208)\n💰薪資待遇💰\n戰鬥加給：5000元\n海勤加給(士兵)：4000元\n海勤加給(士官)：17500元\n💎各階待遇💎\n士兵起薪：44320元\n士官起薪：63950元\n軍官起薪：73060元" )
        line_bot_api.reply_message(event.reply_token, message)   
    elif '%131'in msg:     
        message = TextSendMessage(text="⚓ 海軍一三一艦隊 ⚓\n駐地：基隆軍港\n主力軍艦：\n🇹🇼錦江級巡邏艦🇹🇼\n中華民國海軍與聯合船舶設計發展中心參考海關購自荷蘭的緝私艦（謀星艦、福星艦，現已移交海巡署使用）的設計，並由國內聯合造船廠（已被中信造船購併）建造而成的500噸級巡邏艦，用於近海巡邏之用。\n📃命名方式📃\n錦江級艦後依成軍時間排列計有淡江（淡水河）、新江（新店溪）、鳳江（鳳山溪）、曾江（曾文溪）、高江（高屏溪）、金江、湘江、資江、鄱江、昌江、珠江合計11艘，前六艦之命名係以本島各大名川為主，鄱江、昌江、珠江等後三艦之命名係源於海軍前期汰除之戰功艦，以資紀念，並作為後續艦上官兵之期許，繼志成烈，惕勵奮發，已捍衛我海疆，同級艦型共計12艘。\n-⚓同級艦(舷號)⚓-\n錦江艦(PGG-603)(已除役)\n淡江艦(PGG-605)\n新江艦(PGG-606)\n鳳江艦(PGG-607)\n曾江艦(PGG-608)\n高江艦(PGG-609)\n金江艦(PGG-610)\n湘江艦(PGG-611)\n資江艦(PGG-612)\n鄱江艦(PGG-614)\n昌江艦(PGG-615)\n珠江艦(PGG-617)\n \n \n🇹🇼沱江級巡邏艦🇹🇼\n中華民國海軍的匿蹤雙船體飛彈巡邏艦，可與光華六號飛彈快艇混編執行反艦與反船團任務，也因匿蹤、快速、火力強等特性而被譽為「航母殺手」。\n📃命名方式📃\n民國47年8月23日起共軍日以繼夜砲轟金門，敵艦並猝襲料羅灣，在9月2日的海戰中， 我海軍「維源」、「柳江」、 「沱江」、「美頌」四艦擊沉敵各式艦艇12艘，其中以沱江軍艦擊沉中共艦艇5艘、重傷2艘，戰果最為輝煌，並獲頒海軍第一面榮譽虎旗。\n為紀念「九二海戰」中重創敵艦之沱江軍艦，民國104年4月3日由國人設計建造編號618之「高效能原型艦」，命名為「沱江軍艦」正式成軍，期能承續沱江軍艦光榮傳統，擔負起護衛海疆的重責大任，再創沱江的光榮史頁。\n-⚓同級艦(舷號)⚓-\n沱江艦(PGG-618)\n  \n  \n🇹🇼塔江級巡邏艦🇹🇼\n中華民國海軍沱江級巡邏艦二號艦，簡稱塔江艦、塔江軍艦，為最初中華民國海軍自2014年開始規劃之十二項造艦計畫之一，中華民國海軍稱此計劃為「高效能艦艇後續量產（承海計劃）」，由於與首艦沱江號頗有差異，因此也有將塔江艦為首艦另成一級成為「塔江級巡邏艦」\n📃命名方式📃\n艦名出自台東縣塔瓦溪，取「塔」字搭配中華民國海軍巡邏艦命名模式「江」字而成，亦為至塔江號為止歷來所使用長度最短之河川，中華民國海軍司令部說明，該溪流屬排灣族生活領域，該族人天性具有不畏艱難，秉持著驍勇善戰的精神，足堪本艦官兵效法；另「塔」字象徴此艦擔任海上堡壘，保衛民主自由的中華民國，亦代表國艦國造工作篳路藍縷，積沙成塔，方能建造符合國人期待的優異艦艇。\n-⚓同級艦(舷號)⚓-\n塔江艦(PGG-619)\n  \n \n🇹🇼光華六號飛彈快艇🇹🇼\n簡稱光六，為台灣國際造船（CSBC，簡稱為台船，2007年前名為中國造船公司）為中華民國海軍製造的飛彈快艇，隸屬海軍一三一艦隊，屬於近岸作戰打擊兵力。\n📃命名方式📃  \n 與海鷗飛彈快艇相同，光六艇也僅以編號區別而無命名，共計31艘。\n-⚓同級艦舷號⚓-\nFACG-60~66\nFACG-68~75\nFACG-77~84\nFACG-86~93\n \n💰薪資待遇💰\n戰鬥加給：5000元\n海勤加給(士兵)：4000元\n海勤加給(士官)：17500元\n💎各階待遇💎\n士兵起薪：44320元\n士官起薪：63950元\n軍官起薪：73060元" )
        line_bot_api.reply_message(event.reply_token, message)  
    elif '%146'in msg:     
        message = TextSendMessage(text="⚓ 海軍一四六艦隊 ⚓\n駐地：馬公軍港\n主力軍艦：\n🇹🇼成功級巡防艦🇹🇼\n成功級巡防艦是海軍現役巡防艦，為美國海軍派里級巡防艦的修改型，具有優越靈活之機動力及精良準確之系統，結合現代化之武器裝備，滿足台澎防衛作戰「縱深淺、預警短、決戰快」的特性需求，達到「掌握機先、早期預警、快速反應、指揮作戰的整備目標」，達成鞏固海軍第一線防務為目標。\n📃命名方式📃\n成功級10艘同型艦以中國古代戰將來命名。\n-⚓同級艦(舷號)⚓-\n成功軍艦(PFG-1101)\n鄭和軍艦(PFG-1103)\n繼光軍艦(PFG-1105)\n岳飛軍艦(PFG-1106)\n子儀軍艦(PFG-1107)\n班超軍艦(PFG-1108)\n張騫軍艦(PFG-1109)\n田單軍艦(PFG-1110)\n銘傳軍艦(PFG-1112)\n逢甲軍艦(PFG-1115)\n💰薪資待遇💰\n戰鬥加給：5000元\n海勤加給(士兵)：4000元\n海勤加給(士官)：17500元\n離島加給：7700元\n💎各階待遇💎\n士兵起薪：52020元\n士官起薪：71650元\n軍官起薪：80760元" )
        line_bot_api.reply_message(event.reply_token, message)   
    elif '%168'in msg:     
        message = TextSendMessage(text="⚓ 海軍一六八艦隊 ⚓\n駐地：蘇澳軍港\n主力軍艦：\n🇹🇼紀德級驅逐艦🇹🇼\n    原為美國海軍史普魯恩斯級（Spruance-class）驅逐艦的船身為基礎，但配置不同武裝與電子設備的改良版本。平時基隆級將擔任重要海域偵搜巡邏任務，並擴大其監偵範圍以增加中華民國國軍預警反應時間；戰時主要擔任由不同作戰艦艇組成海軍作戰艦隊旗艦，扼控重要海域阻敵進犯，並可為陸基作戰中心與戰管中心遭受損毀時的備援防空指揮管制任務，進行聯合制空、制海作戰。\n📃命名方式📃\n    最初四艘軍艦的命名原計劃沿用美軍艦名的譯名KIDD為名，再衍生為「德字號」而分別為「紀德」、「明德」、「同德」、「武德」，以彰顯海軍「紀律嚴明，同揚武德」之軍風。於2005年立法院決議，正名以台灣人名或地名，故各艦以台灣四大軍港命名為基隆、蘇澳、左營、馬公；首兩艘艦、為前美軍舷號DDG-995及DDG-994，於2005年12月抵達臺灣，分別命名為「基隆」（DDG-1801）與「蘇澳」(DDG-1802)。三、四為前美軍舷號DDG-993及DDG-996艦於2006年10月25日抵達臺灣，命名為「左營」（DDG-1803）與「馬公」（DDG-1805）。依據命名軍艦級別的傳統，中華民國海軍對其的正式命名為基隆級驅逐艦。\n-⚓同級艦(舷號)⚓-\n基隆軍艦(DDG-1801)\n蘇澳軍艦(DDG-1802)\n左營軍艦(DDG-1803)\n馬公軍艦(DDG-1805)\n💰薪資待遇💰\n戰鬥加給：5000元\n海勤加給(士兵)：4000元\n海勤加給(士官)：17500元\n💎各階待遇💎\n士兵起薪：44320元\n士官起薪：63950元\n軍官起薪：73060元\n  \n \n🇹🇼濟陽級巡防艦🇹🇼\n    為中華民國海軍在1990年代初向美國海軍租借之諾克斯級巡防艦經過後續改良而成的艦型，本級艦的設計以遠洋反潛能力著稱，在中華民國海軍服役以來主要負擔台灣東北部至東部海域的巡防任務，多次偵測行經台灣東部海域之各國潛艦。\n📃命名方式📃\n    依據地名命名法，8艘濟陽級巡防艦分別命名為濟陽(舷號932)、鳳陽(舷號933)、汾陽(舷號934)、蘭陽(舷號935)、海陽(舷號936)、淮陽(舷號937)、宜陽(舷號938)、寧陽(舷號939)。\n-⚓同級艦(舷號)⚓-\n濟陽軍艦(FFG-932)(已除役)\n鳳陽軍艦(FFG-933)\n汾陽軍艦(FFG-934)\n蘭陽軍艦(FFG-935)\n海陽軍艦(FFG-936)(已除役)\n淮陽軍艦(FFG-937)\n寧陽軍艦(FFG-938)\n宜陽軍艦(FFG-939)\n💰薪資待遇💰\n戰鬥加給：5000元\n海勤加給(艙面士兵)：4000元\n海勤加給(艙底士兵)：10000元\n海勤加給(士官)：17500元\n💎各階待遇💎\n艙面士兵起薪：44320元\n艙底士兵起薪：50320\n士官起薪：63950元\n軍官起薪：73060元" )
        line_bot_api.reply_message(event.reply_token, message)   
    elif '%151'in msg:     
        message = TextSendMessage(text="⚓ 海軍一五一艦隊 ⚓\n駐地：左營軍港\n主力軍艦：\n🇹🇼磐石號油彈補給艦🇹🇼\n    全名磐石號快速戰鬥支援艦（英文：Panshi Fast Combat Support Ship)，為中華民國海軍所屬之快速油彈補給艦，名稱典故來於臺灣百岳之磐石山。磐石艦為中華民國海軍自2015年1月23日交艦以來，排水量最大的船艦。\n📃命名方式📃\n名稱典故來於臺灣百岳之磐石山。\n-⚓同級艦(舷號)⚓-\n磐石軍艦(AOE-532)\n \n🇹🇼武夷號油彈補給艦🇹🇼\n    為中華民國海軍的快速油彈補給艦。由台灣國際造船公司承造，艦體設計由美國海軍亨利·J·凱瑟級油料補給艦改造；武夷號是中華民國海軍第一艘專業補給艦，具有專業的海上補給機具，可實施航行間整補，武夷號長期擔負敦睦艦隊旗艦任務，服役迄今已執行十多次敦睦遠航，除擔任艦隊油彈補給外，並擔任文宣展示平台的重要任務。\n-⚓同級艦(舷號)⚓-\n武夷軍艦(AOE-530)\n \n🇹🇼玉山級船塢運輸艦🇹🇼\n    為中華民國海軍執行的十二項造艦計畫（國艦國造）計畫之一，計劃代號「鴻運計畫」，用以取代旭海號船塢登陸艦，首艦於2021年4月13日下水及命名。\n📃命名方式📃\n    下水典禮由總統蔡英文主持，命名「玉山艦（YU SHAN）」，以台灣百岳之首象徵海軍不畏險阻，攀越高峰、追求卓越。\n-⚓同級艦(舷號)⚓-\n玉山軍艦(LPD-1401)\n \n🇹🇼旭海級船塢登陸艦🇹🇼\n    中華民國海軍接收美國海軍安克拉治級船塢登陸艦（Anchorage-class），也是中華民國海軍目前已有兩艘其中之一艘船塢登陸艦。該型艦可協同中和級戰車登陸艦組成快速兩棲運補船團，執行兩棲突擊、逆登陸及快速反應作戰任務。\n📃命名方式📃\n    旭海軍艦命名承襲原鎮海軍艦，以海字為尾命名，選定「旭海」，係以屏東縣牡丹鄉旭海村為命名由來，其目的在感念國人對海軍的關懷與社會大眾對海權的支持。\n-⚓同級艦(舷號)⚓-\n旭海軍艦(LSD-193)\n \n🇹🇼高雄號兩棲指揮艦🇹🇼\n    中華民國海軍旗下一艘現役中的兩棲指揮艦，除了是中華民國海軍唯一的一艘同類型軍艦外，也是第一艘以台灣地名命名的軍艦。\n📃命名方式📃\n    1957年5月租借臺灣，命名為中熙艦，編號LST-219。在1958年八二三砲戰結束後，美軍提供中華民國海軍一套兩棲指揮所需的通信系統組，中熙艦在台灣實施兩棲指揮艦改造工程，1962年1月更名為高雄一號，為海軍第一艘以台灣地名命名的軍艦。\n-⚓同級艦(舷號)⚓-\n高雄軍艦(LCC-1)\n \n🇹🇼中和級戰車登陸艦🇹🇼\n    是一種由中華民國海軍和陸戰隊使用的戰車登陸艦，原為美國海軍新港級坦克登陸艦。主要負責搭載、運送和下卸陸戰隊人員、裝備、補給品及支援兩棲突襲任務。\n-⚓同級艦(舷號)⚓-\n中和軍艦(LST-1180)\n中平軍艦(LST-1181)\n \n🇹🇼中海級戰車登陸艦🇹🇼\n    舊稱為中字號戰車登陸艦[1]，為美國在第二次世界大戰建造的LST二型戰車登陸艦。簡稱L.S.T，俗稱「開口笑」。\n-⚓同級艦(舷號)⚓-\n中建軍艦(LST-205)\n中啟軍艦(LST-218)\n中明軍艦(LST-227)\n中業軍艦(LST-231)\n \n🇹🇼通用登陸艇(合字號)🇹🇼\n    合字號為美國二次大戰建造的坦克登陸艇(LCT),後改稱通用登陸艇(LCU) ;從戰後的1946年起，國府海軍陸續接收了33艘. LCU共有三種規格:一為美製”501”型,其次為日本播磨重工代工製造之”1466”型,及國內獲授權自製的”1610”型,多半都尚在服役中.\n \n \n💰薪資待遇💰\n戰鬥加給：5000元\n海勤加給(士兵)：4000元\n海勤加給(士官)：12000元\n💎各階待遇💎\n士兵起薪：44320元\n士官起薪：58450元\n軍官起薪：67560元" )
        line_bot_api.reply_message(event.reply_token, message)            
    elif '%192'in msg:     
        message = TextSendMessage(text="⚓ 海軍一九二艦隊 ⚓\n駐地：左營軍港\n主力軍艦：\n🇹🇼永豐級獵雷艦🇹🇼\n    中華民國海軍向德國Abeking & Rasmussen公司採購的『MWW50型獵雷艦』，包括四艘同型獵雷艦，每艘造價約近一億德國馬克；船殼為木質外覆強化碳纖維樹脂，艦橋為鋁合金以符合掃雷艦艇低磁性的要求。本級艦最特別的裝備則是所謂的『企鵝』，為類似迷你潛艇的水中遙控除雷載具，它還分為以獵雷聲納偵測傳回資料的A1型及攜帶兩枚100公斤炸彈爆破除雷的B3型兩種。\n📃命名方式📃\n    該級艦名為｢永豐｣，是為了紀念民國初年孫中山為逃避陳炯明事變所乘之船艦，是時蔣介石亦登上此艦協助指揮督統作戰。隨後此艦改名為｢中山艦｣，最後於對日抗戰時被日軍擊沉於長江江底。\n-⚓同級艦(舷號)⚓-\n永豐軍艦(MHC-1301)\n永嘉軍艦(MHC-1302)\n永定軍艦(MHC-1303)\n永順軍艦(MHC-1305)\n \n🇹🇼永豐級獵雷艦🇹🇼\n    中華民國於1993年向美國購買的4艘掃雷艦，原為美國海軍的進取級掃雷艦。船殼為三層松木包覆，木質外殼具備較佳的低磁性需求，同時多層外殼也具有較好的水雷爆炸震波吸收能力。本級艦偵測水雷主要裝備仰仗AN/SQQ-14|AN/SQQ-14可變深度聲納，該型聲納具有高頻及低頻等2種操作模式，最大偵測距離約1,800碼（1,646公尺）。\n📃命名方式📃\n    以「永」字頭來命名，稱為永陽級，編號則接續永豐級獵雷艦。\n-⚓同級艦(舷號)⚓-\n永陽軍艦(MSO-1306)\n \n🇹🇼永靖級獵雷艦🇹🇼\n    由中華民國海軍所操作的獵雷艦（近岸獵雷艦）級別，隸屬海軍一九二艦隊。其前身原本是美國海軍的鶚級獵雷艦（Osprey-class coastal minehunter），800噸級的此級船艦，除了尺碼噸位超過一般獵雷艦的平均水準外，配備較新穎的高精度聲納等設備也是另一個特色。\n📃命名方式📃\n    在2010年1月29日，美國國務院正式宣布一批對台軍售，其中包含兩艘鶚級獵雷艦，價值1億500萬美元 （其中金鶯號價值626萬美元，隼號價格578萬美元，約略相當於原始造價的5%），兩艦被命名為永靖級，其中原本金鶯號被命名為永靖（MHC-1310），原隼號命名為永安號（MHC-1311），同年10月26日成軍。\n-⚓同級艦(舷號)⚓-\n永靖軍艦(MHC-1310)\n永安軍艦(MHC-1311)\n \n🇹🇼達觀號海洋測量艦🇹🇼\n　　中華民國交通部代海軍於1994年向義大利購買的海洋測量艦。平時以台灣海峽週邊海域專屬經濟海域與海南諸島之航道測量與水文資料蒐集任務為主，必要時支援國內、國際海洋研究計畫及臨時賦予之任務。\n📃命名方式📃\n    以桃園達觀山命名\n-⚓同級艦(舷號)⚓-\n達觀軍艦(AGS-1601)\n \n🇹🇼快速布雷艇🇹🇼\n快速布雷艇（研製計畫代號為「永捷」）可在短時間內布放大量水雷，對敵方水面艦與登陸船團造成威脅。可進出船塢登陸艦。儎臺需具備可裝儎本軍現行水雷武器之能力；另需配置反水面作戰之武器裝備。具備導航及定位能力，定位信號涵蓋範圍廣、信源穩定、接收便捷，以符布雷作業定位要求。\n-⚓同級艦(舷號)⚓-\nFMLB-1\nFMLB-2\nFMLB-3\nFMLB-5\n \n🇹🇼大湖級救難艦🇹🇼\n　　又稱為大字號救難艦，為中華民國海軍輔助艦艇。大湖艦（ARS-552；原美國海軍Diver級救難艦，Grapple號，ARS-7），美國加州Basalt Rock廠建造，1942年12月31日下水，1943年12月16日成軍，1977年退役，同年12月1日於夏威夷移交中華民國海軍，（原編號ARS-7後改ARS-552），1978年2月21日返抵左營港。大屯艦（ARS-556；原美國海軍Bolster級救難艦，Recovery號，ARS-43），1945年8月4日下水，1946年5月15日成軍，1994年9月20日退役，1998年9月30日移交中華民國海軍，1999年3月1日在基隆「海軍第三造船廠」船塢啟封。同時也是改編史實電影《怒海潛將》的使用船艦，美國海軍第一位黑人潛水員布拉希爾士官長（《怒海潛將》男主角）曾在大屯軍艦服役。\n-⚓同級艦(舷號)⚓-\n大湖軍艦(ARS-552)\n大屯軍艦(ARS-556)\n \n🇹🇼大同級遠洋拖船🇹🇼\n    中華民國海軍輔助艦艇，主要用途是拖救各級軍艦（潛艦除外）和支援打靶勤務。配備10噸吊桿、150噸主拖纜機、兩個各重達四噸的易式錨和各式拖纜與救難裝備，在中華民國海軍服役期間，小至港勤拖船、飛彈快艇，大至巡防艦、補給艦，都曾接受大同級的服務。本級艦為美國海軍在第二次世界大戰前後建造的艦隊遠洋拖船（Fleet Ocean Tug）。與先前的遠洋拖船設計相比，全長65公尺、全寬38公尺的較大尺寸，更大的油箱容量和首次應用於美國海軍大型水面艦的柴電驅動系統，使得本級艦更能夠應付長時間長距離的遠洋拖救任務。美國海軍第一位黑人潛水員布拉希爾士官長（電影《怒海潛將》主角）曾在大台軍艦服役。\n-⚓同級艦(舷號)⚓-\n大萬軍艦(ATF-551)\n大岡軍艦(ATF-554)\n大台軍艦(ATF-563)\n \n💰薪資待遇💰\n戰鬥加給：5000元\n海勤加給(士兵)：4000元\n海勤加給(士官)：12000元\n💎各階待遇💎\n士兵起薪：44320元\n士官起薪：58450元\n軍官起薪：67560元\n \n \n🇹🇼海軍水下作業大隊🇹🇼\n 中華民國海軍轄下的一支海事救難與未爆彈處理部隊，主要負責水底搜索、潛水拯救及爆炸品處理。當災害發生時，以他們的水中專業將災民救出危險的地方。還能夠進行一些船艦的維修任務，與排除港灣中的障礙物。\n \n💰薪資待遇💰\n戰鬥加給：3000元\n海勤加給(作業隊士兵)：4000元\n海勤加給(作業隊士官)：12000元\n海勤加給(械彈處理中隊士兵)：15000元\n海勤加給(械彈處理中隊士官)：17500元\n💎各階待遇💎\n作業隊士兵起薪：42320元\n作業隊士官起薪：56450元\n作業隊軍官起薪：65560元\n械彈處理中隊士兵起薪：53320元\n械彈處理中隊士官起薪：61950元\n械彈處理中隊軍官起薪：71060元" )
        line_bot_api.reply_message(event.reply_token, message)
    elif '%256'in msg:     
        message = TextSendMessage(text="⚓ 海軍二五六戰隊 ⚓\n駐地：左營軍港\n主力軍艦：\n🇹🇼茄比級潛艦🇹🇼\n    中華民國海軍兩艘潛艦海獅號及海豹號之非正式統稱，亦有另名海獅級潛艦。雖然此二艘潛艦實際上屬於不同的設計，但均接受過茄比（水下推進能力改進計劃，縮寫GUPPY）2號現代化工程，所以被稱為「茄比級」，並持續於中華民國海軍服役中。茄比級潛艦為目前全世界現役柴電潛艦中最老的，兩艘潛艦皆已服役超過70年，創下世界唯一參與過二次世界大戰仍在役的紀錄。\n-⚓同級艦(舷號)⚓-\n海獅號(SS-791)\n海豹號(SS-792)\n \n🇹🇼劍龍級潛艦🇹🇼\n    中華民國海軍向荷蘭購買的潛艦。由荷蘭劍魚級潛艦（或稱旗魚級）降級裝備改裝而成，再加上海象級潛艦的技術，但仍維持劍魚級使用的淚滴型艦身、十字型尾鰭。\n-⚓同級艦(舷號)⚓-\n海龍號(SS-793)\n海虎號(SS-794)\n \n \n💰薪資待遇💰\n戰鬥加給：5000元\n海勤加給(士兵)：20000元\n海勤加給(士官)：37000元\n海勤加給(士官長)：41000元\n💎各階待遇💎\n士兵起薪：60320元\n士官起薪：83450元\n士官長起薪：97460元\n軍官起薪：96560元" )
        line_bot_api.reply_message(event.reply_token, message)
   #地面作戰部隊簡介   
    elif '%戰搜'in msg:     
        message = TextSendMessage(text="✈︎ 海軍海上戰術偵搜大隊 ✈︎\n駐地：空軍屏東基地✈︎\n🗊單位沿革🗊\n    原為中華民國陸軍航空特戰指揮部戰術偵搜大隊(R.O.C.Army Tactical Reconnaissance Group)，以國家中山科學研究院研發的銳鳶無人機為主要裝備，銳鳶無人機相關裝備及操作人員全都移撥給海軍，運用具備「損小、效高、易行、價廉」之裝備，可強化聯合監偵作業機制及不對稱作戰戰力，俾以提升聯合作戰效益，爭取預警與反應時間。\n \n🔱主力裝備🔱\n🇹🇼銳鳶無人機🇹🇼\n \n⚔指揮體系⚔\n教勤中隊\n偵搜一中隊\n偵搜二中隊\n偵搜三中隊\n \n  \n💰薪資待遇💰\n戰鬥加給：5000元\n💎各階待遇💎\n士兵起薪：40320元\n士官起薪：46450元\n軍官起薪：55560元" )
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



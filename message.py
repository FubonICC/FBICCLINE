#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#ImagemapSendMessage(圖片地圖訊息)
def imagemap_message():
    message = ImagemapSendMessage(
        base_url="https://i.imgur.com/J5DELEi.jpg",
        alt_text='人才招募中心服務選單',
        base_size=BaseSize(width=1040, height=664),
        actions=[
            URIImagemapAction(
                #預約體檢
                link_uri="https://rdrc.mnd.gov.tw/rdrcnew/tpry/healthreserve.asp?item=92",
                area=ImagemapArea(
                    x=0, y=0, width=520, height=332
                )
            ),
            URIImagemapAction(
                #線上報名
                link_uri="https://rdrc.mnd.gov.tw/news/OnlineSystem?Module=1043",
                area=ImagemapArea(
                    x=520, y=0, width=520, height=332
                )
            ),
            URIImagemapAction(
                #線上測驗
                link_uri="https://rdrc.mnd.gov.tw/RDRCExamWeb/index.aspx",
                area=ImagemapArea(
                    x=0, y=332, width=520, height=332
                )
            ),
            URIImagemapAction(
                #資格媒合
                link_uri="https://rdrc.mnd.gov.tw/Suit",
                area=ImagemapArea(
                    x=520, y=332, width=520, height=332
                )
            ),
        ]
    )
    return message

#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def buttons_message():
    message = TemplateSendMessage(
        alt_text='好消息來囉～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://navy.mnd.gov.tw/Photo/Ban/202105051632_534790.jpg",
            title="迫不急待加入海軍了嗎？",
            text="輸入生日後即獲得抽獎機會",
            actions=[
                DatetimePickerTemplateAction(
                    label="請選擇生日",
                    data="input_birthday",
                    mode='date',
                    initial='1990-01-01',
                    max='2019-03-10',
                    min='1930-01-01'
                ),
                MessageTemplateAction(
                    label="看抽獎品項",
                    text="有哪些抽獎品項呢？"
                ),
                URITemplateAction(
                    label="填寫報名意願書",
                    uri="https://forms.gle/8AEvmB8hhHxByfhg7"
                )
            ]
        )
    )
    return message


#TemplateSendMessage - ButtonsTemplate (開場按鈕訊息)
def buttons_message1():
    message = TemplateSendMessage(
        alt_text='歡迎來到富邦大無疆C館',
        template=ButtonsTemplate(
            thumbnail_image_url="https://upload.cc/i1/2022/12/19/afREkl.jpg",
            title="🇹🇼富邦大無疆C館小管家🏠",
            text="請選擇你要的服務",
            actions=[
                URITemplateAction(
                    label="我想了解規約",
                    uri="https://online.fliphtml5.com/bbblu/rdib/"
                ),
                MessageTemplateAction(
                    label="公設管理辦法",
                    text="公設管理"
                ),
                URITemplateAction(
                    label="意見填寫",
                    uri="https://forms.gle/zHanAfpayZUpZZCh8"
                )
            ]
        )
    )
    return message

def buttons_message2():
    message = TemplateSendMessage(
        alt_text='管理委員會',
        template=ButtonsTemplate(
            thumbnail_image_url="https://upload.cc/i1/2023/02/01/46eVhs.jpg",
            title="🏢管理委員會🏢",
            text="富邦大無疆C館管理委員會",
            actions=[
                MessageTemplateAction(
                    label="現任管理委員會成員",
                    text="管委會成員"
                ),
                URITemplateAction(
                    label="歷任管委會",
                    uri="https://online.fliphtml5.com/bbblu/rdib/"
                )
            ]
        )
    )
    return message

#def buttons_message3():
#    message = TemplateSendMessage(
#        alt_text='海軍官網',
#        template=ButtonsTemplate(
#            thumbnail_image_url="https://i.imgur.com/l6tGJCx.png",
#            title="🇹🇼中華民國海軍官方網站🇹🇼",
#            text="還用問嗎？通通加就對了！",
#            actions=[
#                URITemplateAction(
#                    label="海軍官方網站",
#                    uri='https://navy.mnd.gov.tw/index.aspx'
#                ),
#                URITemplateAction(
#                    label="海軍Facebook",
#                    uri='https://www.facebook.com/ROCNAVY.tw'
#                ),
#                URITemplateAction(
#                    label="海軍Instagram",
#                    uri='https://www.instagram.com/r.o.c.navy/'
#                )
#            ]
#        )
#    )
#    return message



#TemplateSendMessage - ConfirmTemplate(確認介面訊息)
def Confirm_Template():

    message = TemplateSendMessage(
        alt_text='你要找富邦小管家程式小編嗎？',
        template=ConfirmTemplate(
            text="你要找小管家的程式小編兼副主委嗎？",
            actions=[
                MessageTemplateAction(
                    label="是的，他是誰？",
                    text="小編",
                ),
                MessageTemplateAction(
                    label="查詢其他功能",
                    text="查詢其他功能"
                )
            ]
        )
    )
    return message

#旋轉木馬按鈕訊息介面

def Carousel_Template1():
    message = TemplateSendMessage(
        alt_text='公設管理',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://upload.cc/i1/2022/12/20/S6tBiL.jpg',
                    title='健身房',
                    text='健身房管理辦法',
                    actions=[
                        MessageAction(
                            label='區域：南部',
                            text='南部地區'
                        ),
                        MessageAction(
                            label='詳細說明',
                            text='%124'
                        ),
                        URITemplateAction(
                            label='隊徽&組織沿革',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30029&AID=30045'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.cc/i1/2022/12/20/Y9pfIa.jpg',
                    title='游泳池',
                    text='游泳池管理辦法',
                    actions=[
                        MessageAction(
                            label='區域：北部',
                            text='北部地區'
                        ),
                        MessageAction(
                            label='詳細說明',
                            text='%131'
                        ),
                        URITemplateAction(
                            label='隊徽&組織沿革',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30029&AID=30050'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.cc/i1/2022/12/20/oLcdpa.jpg',
                    title='瑜珈教室',
                    text='琴房管理辦法',
                    actions=[
                        MessageAction(
                            label='區域：離島',
                            text='離島地區'
                        ),
                        MessageAction(
                            label='詳細說明',
                            text='%146'
                        ),
                        URITemplateAction(
                            label='隊徽&組織沿革',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30029&AID=30047'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.cc/i1/2022/12/20/58DVke.jpg',
                    title='琴房',
                    text='琴房管理辦法',
                    actions=[
                        MessageAction(
                            label='區域：離島',
                            text='離島地區'
                        ),
                        MessageAction(
                            label='詳細說明',
                            text='%146'
                        ),
                        URITemplateAction(
                            label='隊徽&組織沿革',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30029&AID=30047'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.cc/i1/2022/12/20/ln5wyZ.jpg',
                    title='閱覽室',
                    text='閱覽室管理辦法',
                    actions=[
                        MessageAction(
                            label='區域：南部',
                            text='南部地區'
                        ),
                        MessageAction(
                            label='詳細說明',
                            text='%151'
                        ),
                        URITemplateAction(
                            label='隊徽&組織沿革',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30029&AID=30051'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.cc/i1/2022/12/20/ra0jHi.jpg',
                    title='戶外吸菸區',
                    text='本社區設有戶外吸菸區兩處',
                    actions=[
                        MessageAction(
                            label='戶外吸菸區',
                            text='戶外吸菸區'
                        ),
                        MessageAction(
                            label='詳細說明',
                            text='%168'
                        ),
                        URITemplateAction(
                            label='隊徽&組織沿革',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30029&AID=30049'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.cc/i1/2022/12/20/UBOTGd.jpg',
                    title='多功能退縮空間',
                    text='中華郵政I郵箱、統一販賣機、黑松販賣機、舊衣回收箱',
                    actions=[
                        MessageAction(
                            label='區域：南部',
                            text='南部地區'
                        ),
                        MessageAction(
                            label='I郵箱簡易說明',
                            text='I郵箱'
                        ),
                        URITemplateAction(
                            label='中華郵政I郵箱官方網站',
                            uri='https://ezpost.post.gov.tw/ibox/tariff.aspx#box26'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.cc/i1/2022/12/20/fydqTN.jpg',
                    title='寵物洗滌區',
                    text='提供住戶清洗寵戶好夥伴的地方',
                    actions=[
                        MessageAction(
                            label='位置： H棟後方中庭區域',
                            text='寵物洗滌區'
                        ),
                        MessageAction(
                            label='使用說明',
                            text='寵物洗滌區使用說明'
                        ),
                        URITemplateAction(
                            label='中華郵政I郵箱官方網站',
                            uri='https://ezpost.post.gov.tw/ibox/tariff.aspx#box26'
                        )
                    ]
                ),
            ]
        )
    )
    return message

def Carousel_Template2():
    message = TemplateSendMessage(
        alt_text='生活公約',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/dA6kJYp.jpg',
                    title='社區管理辦法',
                    text='富邦大無疆C館管理辦法',
                    actions=[   
                        URITemplateAction(
                            label='詳細內容',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30151&AID=30329'
                        ),
                        PostbackTemplateAction(
                            label='\s',
                            data='A'
                        ),
                        PostbackTemplateAction(
                            label='\s',
                            data='A'                            
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/dA6kJYp.jpg',
                    title='社區生活公約',
                    text='富邦大無疆C館生活公約',
                    actions=[   
                        URITemplateAction(
                            label='詳細內容',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30151&AID=30329'
                        ),
                        PostbackTemplateAction(
                            label='\s',
                            data='A'
                        ),
                        PostbackTemplateAction(
                            label='\s',
                            data='A'                            
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/dA6kJYp.jpg',
                    title='自行車停車位管理辦法',
                    text='自行車停車位管理辦法%申請書',
                    actions=[   
                        URITemplateAction(
                            label='管理辦法',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30151&AID=30329'
                        ),
                        URITemplateAction(
                            label='申請書下載',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30151&AID=30329'
                        ),
                        PostbackTemplateAction(
                            label='\s',
                            data='A'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/dA6kJYp.jpg',
                    title='門禁管制辦法',
                    text='富邦大無疆C館生活公約',
                    actions=[   
                        URITemplateAction(
                            label='門禁管制辦法',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30151&AID=30329'
                        ),
                        URITemplateAction(
                            label='磁卡及車道遙控器申請辦法',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30151&AID=30329'
                        ),
                        PostbackTemplateAction(
                            label='\s',
                            data='A'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/4OpUD9p.jpg',
                    title='廣告招商',
                    text='社區廣告招商資訊',
                    actions=[  
                        URITemplateAction(
                            label='電梯公佈欄招商資訊',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30151&AID=30331'
                        ),
                        PostbackTemplateAction(
                            label='\s',
                            data='A'
                        ),
                        PostbackTemplateAction(
                            label='\s',
                            data='A'
                        )
                    ]
                )
            ]
        )
    )
    return message

def Carousel_Template3():
    message = TemplateSendMessage(
        alt_text='第二屆管理委員會成員列表',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/7/71/UAV_9717_Display_at_No.11_Pier_Left_Rear_View_20130504.jpg',
                    title='郭晉叡',
                    text='主任委員-郭晉叡',
                    actions=[
                        PostbackTemplateAction(
                            label='ˇ棟別-H',
                            data='A'
                        ),                    
                         MessageAction(
                            label='聯絡資訊',
                            text='%聯絡主委'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://navy.mnd.gov.tw/Photo/OtherHTML/201610261134_976298.jpg',
                    title='邱偉倫',
                    text='副主任委員-邱偉倫',
                    actions=[
                        PostbackTemplateAction(
                            label='棟別-F',
                            data='A'
                        ),
                         MessageAction(
                            label='聯絡資訊',
                            text='%聯絡副主委'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/4cwtrFf.jpg',
                    title='許登欽',
                    text='監察委員-許登欽',
                    actions=[
                        PostbackTemplateAction(
                            label='棟別-E',
                            data='A'
                        ),
                        MessageAction(
                            label='詳細說明',
                            text='%海偵'
                        ),
                         MessageAction(
                            label='聯絡資訊',
                            text='%聯絡監委'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2021/12/26/realtime/14886452.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=800&exp=3600&w=930&nt=1',
                    title='海軍海鋒大隊',
                    text='海軍飛彈部隊',
                    actions=[
                        PostbackTemplateAction(
                            label='區域：北、中、南部、外島、離島',
                            data='這是ID=2'
                        ),
                        MessageAction(
                            label='詳細說明',
                            text='%海鋒'
                        ),
                        URITemplateAction(
                            label='前往網頁',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30029&AID=30056'
                        )
                    ]
                ),
            ]
        )
    )
    return message


def Carousel_Template4():
    message = TemplateSendMessage(
        alt_text='海軍一般陸岸單位',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/RPMGYzw.jpg',
                    title=' 海軍教育訓練暨準則發展指揮部',
                    text='海軍新兵訓練中心、海軍技術學校\n海軍陸戰隊新兵訓練中心、海軍陸戰隊學校',
                    actions=[
                        PostbackTemplateAction(
                            label='區域：南部地區',
                            data='A'
                        ),
                         MessageAction(
                            label='詳細說明',
                            text='%教準部'
                        ),                       
                        URITemplateAction(
                            label='前往網頁',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_List.aspx?ID=30155'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/tg01yeu.jpg',
                    title='海軍保修指揮部',
                    text='左營後勤支援指揮部、蘇澳後勤支援指揮部\n基隆後勤支援指揮部、馬公後勤支援指揮部\n戰鬥系統工廠、補給總庫',
                    actions=[
                        PostbackTemplateAction(
                            label='區域：北部、南部、離島',
                            data='這是ID=2'
                        ),
                        MessageAction(
                            label='詳細說明',
                            text='%保指部'
                        ),
                        URITemplateAction(
                            label='前往網頁',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30090&AID=30142'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://navy.mnd.gov.tw/Photo/PartnerHTML/201902210941_1489.jpg',
                    title='海軍通信系統指揮部',
                    text='海軍版中華電信',
                    actions=[
                        PostbackTemplateAction(
                            label='區域：北部、南部、離島',
                            data='這是ID=2'
                        ),
                        MessageAction(
                            label='詳細說明',
                            text='%通指部'
                        ),
                        URITemplateAction(
                            label='前往網頁',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30075&AID=30126'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.chinatimes.com/newsphoto/2018-10-10/1024/20181010001186.jpg',
                    title='司令部勤務大隊',
                    text='海軍儀隊、海軍樂隊\n汽車隊、勤務隊',
                    actions=[
                        PostbackTemplateAction(
                            label='區域：北部',
                            data='這是ID=2'
                        ),
                        MessageAction(
                            label='詳細說明',
                            text='%勤務大隊'
                        ),
                        URITemplateAction(
                            label='前往網頁',
                            uri='https://navy.mnd.gov.tw/AboutUs/About_Info.aspx?ID=30057&CID=30072'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/ln2W9Id.jpg',
                    title='大氣海洋局',
                    text='風雲審天機 滄海探奧義',
                    actions=[
                        PostbackTemplateAction(
                            label='區域：南部',
                            data='這是ID=2'
                        ),
                        MessageAction(
                            label='詳細說明',
                            text='%大氣'
                        ),
                         MessageAction(
                            label='隊徽及照片',
                            text='%圖庫大氣'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/z8t8tXr.jpg',
                    title='海軍造船發展中心',
                    text='國艦國造戰力強',
                    actions=[
                        PostbackTemplateAction(
                            label='區域：南部',
                            data='這是ID=2'
                        ),
                        MessageAction(
                            label='詳細說明',
                            text='%海發'
                        ),
                        URITemplateAction(
                            label='前往網頁',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30050&AID=30046'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://www.cna.edu.tw/upload/CMS/20141212163254281.jpg',
                    title='海軍官校',
                    text='海軍菁英幹部新手村',
                    actions=[
                        PostbackTemplateAction(
                            label='區域：南部',
                            data='這是ID=2'
                        ),
                        MessageAction(
                            label='詳細說明',
                            text='%海官'
                        ),
                        URITemplateAction(
                            label='前往網頁',
                            uri='https://www.cna.edu.tw/tw/index.php'
                        )
                    ]
                ),
            ]
        )
    )
    return message


#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)
def image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='圖片旋轉木馬',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/CfQUgR3.png",
                    action=URITemplateAction(
                        label="隊徽",
                        uri="https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30029&AID=42132"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/F1drsXQ.jpg",
                    action=URITemplateAction(
                        label="點此放大",
                        uri="https://i.imgur.com/F1drsXQ.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/RbA7gnG.jpg",
                    action=URITemplateAction(
                        label="點此放大",
                        uri="https://i.imgur.com/RbA7gnG.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/A9NsmKb.jpg",
                    action=URITemplateAction(
                        label="點此放大",
                        uri="https://i.imgur.com/A9NsmKb.jpg"
                    )
                )
            ]
        )
    )
    return message

def image_carousel_message2():
    message = TemplateSendMessage(
        alt_text='大氣海洋局',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QAPaXwy.jpg",
                    action=URITemplateAction(
                        label="隊徽",
                        uri="https://cnmoo.mnd.gov.tw/Default.aspx"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/lvdTBBk.jpg",
                    action=URITemplateAction(
                        label="點此放大",
                        uri="https://i.imgur.com/lvdTBBk.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/3K9YntV.jpg",
                    action=URITemplateAction(
                        label="點此放大",
                        uri="https://i.imgur.com/3K9YntV.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/TRm1AJS.jpg",
                    action=URITemplateAction(
                        label="點此放大",
                        uri="https://i.imgur.com/TRm1AJS.jpg"
                    )                
                ),
                 ImageCarouselColumn(
                    image_url="https://i.imgur.com/4GdAaUs.jpg",
                    action=URITemplateAction(
                        label="點此放大",
                        uri="https://i.imgur.com/4GdAaUs.jpg"
                    )  
                ),
                 ImageCarouselColumn(
                    image_url="https://i.imgur.com/RYld662.jpg",
                    action=URITemplateAction(
                        label="點此放大",
                        uri="https://i.imgur.com/RYld662.jpg"
                    )  
                ),
            ]
        )
    )
    return message

def image_carousel_message3():
    message = TemplateSendMessage(
        alt_text='色弱測驗',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/cMRuwnZ.jpg",
                    action=URITemplateAction(
                        label="開始測試",
                        uri="https://online.fliphtml5.com/stwml/blro/"
                    )
                )
            ]
        )
    )
    return message


#關於LINEBOT聊天內容範例
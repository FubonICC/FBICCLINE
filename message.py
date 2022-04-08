#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#ImagemapSendMessage(組圖訊息)
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

#ImagemapSendMessage(組圖訊息)
def imagemap_message01():
    message = ImagemapSendMessage(
        base_url="https://i.imgur.com/BfTFVDN.jpg",
        alt_text='最新的合作廠商有誰呢？',
        base_size=BaseSize(height=2000, width=2000),
        actions=[
            URIImagemapAction(
                #家樂福
                link_uri="https://tw.shop.com/search/%E5%AE%B6%E6%A8%82%E7%A6%8F",
                area=ImagemapArea(
                    x=0, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #生活市集
                link_uri="https://tw.shop.com/search/%E7%94%9F%E6%B4%BB%E5%B8%82%E9%9B%86",
                area=ImagemapArea(
                    x=1000, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #阿瘦皮鞋
                link_uri="https://tw.shop.com/search/%E9%98%BF%E7%98%A6%E7%9A%AE%E9%9E%8B",
                area=ImagemapArea(
                    x=0, y=1000, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #塔吉特千層蛋糕
                link_uri="https://tw.shop.com/search/%E5%A1%94%E5%90%89%E7%89%B9",
                area=ImagemapArea(
                    x=1000, y=1000, width=1000, height=500
                )
            ),
            URIImagemapAction(
                #亞尼克生乳捲
                link_uri="https://tw.shop.com/search/%E4%BA%9E%E5%B0%BC%E5%85%8B",
                area=ImagemapArea(
                    x=1000, y=1500, width=1000, height=500
                )
            )
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
        alt_text='歡迎來到海軍招募讚',
        template=ButtonsTemplate(
            thumbnail_image_url="https://navy.mnd.gov.tw/Photo/Ban/202105051632_534790.jpg",
            title="🇹🇼海軍招募讚服務選單🇹🇼",
            text="請選擇你要的服務",
            actions=[
                MessageTemplateAction(
                    label="我要認識海軍艦隊",
                    text="認識海軍"
                ),
                MessageTemplateAction(
                    label="認識海軍陸岸單位",
                    text="陸岸"
                ),
                MessageTemplateAction(
                    label="招募中心服務選單",
                    text="中心服務"
                ),
                URITemplateAction(
                    label="填寫報名意願書",
                    uri="https://forms.gle/8AEvmB8hhHxByfhg7"
                )
            ]
        )
    )
    return message

def buttons_message2():
    message = TemplateSendMessage(
        alt_text='歡迎來到海軍招募讚',
        template=ButtonsTemplate(
            thumbnail_image_url="https://navy.mnd.gov.tw/Photo/Ban/202105051632_534790.jpg",
            title="🇹🇼中華民國海軍單位介紹🇹🇼",
            text="請選擇你想了解的單位類型",
            actions=[
                MessageTemplateAction(
                    label="海軍艦隊",
                    text="海軍艦隊"
                ),
                MessageTemplateAction(
                    label="海軍陸岸作戰單位",
                    text="陸岸作戰"
                ),
                MessageTemplateAction(
                    label="海軍陸岸一般單位",
                    text="陸岸一般"
                ),
                MessageTemplateAction(
                    label="海軍陸戰隊單位",
                    text="海軍陸戰隊"
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ConfirmTemplate(確認介面訊息)
def Confirm_Template():

    message = TemplateSendMessage(
        alt_text='是否註冊成為會員？',
        template=ConfirmTemplate(
            text="是否註冊成為會員？",
            actions=[
                PostbackTemplateAction(
                    label="馬上註冊",
                    text="現在、立刻、馬上",
                    data="會員註冊"
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
        alt_text='海軍艦隊',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://navy.mnd.gov.tw/Photo/PartnerHTML/201612151209_194894.jpg',
                    title='海軍一二四艦隊',
                    text='主力軍艦：康定級軍艦',
                    actions=[
                        MessageAction(
                            label='駐地：左營軍港',
                            text='左營軍港'
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
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/8/8e/ROCN_Ta_Chiang.png',
                    title='海軍一三一艦隊',
                    text='主力軍艦：錦江級軍艦、沱江級軍艦、塔江級軍艦、光華六號飛彈快艇',
                    actions=[
                        MessageAction(
                            label='駐地：基隆軍港',
                            text='基隆軍港'
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
                    thumbnail_image_url='https://cdn2.ettoday.net/images/326/d326819.jpg',
                    title='海軍一四六艦隊',
                    text='主力軍艦：成功級軍艦',
                    actions=[
                        MessageAction(
                            label='駐地：馬公軍港',
                            text='馬公軍港'
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
                    thumbnail_image_url='https://imgcdn.cna.com.tw/www/WebPhotos/1024/20210413/1171x768_47493734004.jpg',
                    title='海軍一五一艦隊',
                    text='主力軍艦：兩棲登陸艦艇、油彈補給艦',
                    actions=[
                        MessageAction(
                            label='駐地：左營軍港',
                            text='左營軍港'
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
                    thumbnail_image_url='https://tnimage.s3.hicloud.net.tw/photos/shares/jimi0611/20130927/5781627.jpg',
                    title='海軍一六八艦隊',
                    text='主力軍艦：紀德級驅逐艦、濟陽級巡防艦',
                    actions=[
                        MessageAction(
                            label='駐地：蘇澳軍港',
                            text='蘇澳軍港'
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
                    thumbnail_image_url='https://s.yimg.com/ny/api/res/1.2/rsY778kfLW8GSWKkcnJK3Q--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTU0MDtjZj13ZWJw/https://s.yimg.com/uu/api/res/1.2/m2So_wC8mFV5Q0JeyUSTNQ--~B/aD00NTA7dz04MDA7YXBwaWQ9eXRhY2h5b24-/https://media.zenfs.com/en/cna.com.tw/633e3f9666bc2096512d8c51cccb6e31',
                    title='海軍一九二艦隊',
                    text='主力軍艦：快速布雷艇、掃/獵雷艦、海洋測量艦、救難艦、遠洋拖船、水下作業大隊',
                    actions=[
                        MessageAction(
                            label='駐地：左營軍港',
                            text='左營軍港'
                        ),
                        MessageAction(
                            label='詳細說明',
                            text='%192'
                        ),
                        URITemplateAction(
                            label='隊徽&組織沿革',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30029&AID=30052'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://cdn2.ettoday.net/images/3418/d3418257.jpg',
                    title='海軍二五六戰隊',
                    text='主力軍艦：茄比級潛艦、劍龍級潛艦',
                    actions=[
                        MessageAction(
                            label='駐地：左營軍港',
                            text='左營軍港'
                        ),
                        MessageAction(
                            label='詳細說明',
                            text='%256'
                        ),
                        URITemplateAction(
                            label='隊徽&組織沿革',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30029&AID=30053'
                        )
                    ]
                ),
            ]
        )
    )
    return message

def Carousel_Template2():
    message = TemplateSendMessage(
        alt_text='海軍陸戰隊',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://navy.mnd.gov.tw/Photo/PartnerHTML/201612211656_260768.png',
                    title='陸戰九九旅',
                    text='鐵軍：鋼鐵勁旅，防衛固守，有如銅牆鐵壁之堅強勁旅',
                    actions=[
                        PostbackTemplateAction(
                            label='駐地：林園',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是1'
                        ),
                        URITemplateAction(
                            label='了解陸戰九九旅',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30151&AID=30329'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuo7n2_HNSFuT3T7Z9PUZmn1SDM6G6-iXfRC3FxdGTj7X1Wr0RzA',
                    title='這是第二塊模板',
                    text='副標題可以自己改',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=2'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是2'
                        ),
                        URITemplateAction(
                            label='進入2的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Number_2_in_light_blue_rounded_square.svg/200px-Number_2_in_light_blue_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png',
                    title='這是第三個模塊',
                    text='最多可以放十個',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=3'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是3'
                        ),
                        URITemplateAction(
                            label='uri2',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png'
                        )
                    ]
                )
            ]
        )
    )
    return message

def Carousel_Template3():
    message = TemplateSendMessage(
        alt_text='海軍陸岸作戰單位',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/7/71/UAV_9717_Display_at_No.11_Pier_Left_Rear_View_20130504.jpg',
                    title='海軍海上戰術偵搜大隊',
                    text='銳鳶無人機',
                    actions=[
                        PostbackTemplateAction(
                            label='駐地：屏東空軍基地',
                            data='A'
                        ),
                         MessageAction(
                            label='詳細說明',
                            text='%戰搜'
                        ),                       
                        URITemplateAction(
                            label='前往網頁',
                            uri='https://zh.wikipedia.org/wiki/%E4%B8%AD%E8%8F%AF%E6%B0%91%E5%9C%8B%E6%B5%B7%E8%BB%8D%E6%B5%B7%E4%B8%8A%E6%88%B0%E8%A1%93%E5%81%B5%E8%92%90%E5%A4%A7%E9%9A%8A'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://navy.mnd.gov.tw/Photo/OtherHTML/201610261134_976298.jpg',
                    title='海軍反潛航空大隊',
                    text='S-70C反潛直升機、500MD反潛直昇機',
                    actions=[
                        PostbackTemplateAction(
                            label='駐地：左營',
                            data='這是ID=2'
                        ),
                        MessageAction(
                            label='詳細說明',
                            text='%反潛'
                        ),
                        URITemplateAction(
                            label='前往網頁',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30029&AID=30057'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.6435-9/126933144_1746128488898865_1472026323777596786_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=8bfeb9&_nc_ohc=ufSob08X-pkAX_x7kDe&_nc_ht=scontent.fkhh1-1.fna&oh=00_AT8K51NCTW9jyHCVlP1DJnAUQufMhV9356ZupivPXlxoqg&oe=624FDFD3',
                    title='海軍海洋監偵指揮部',
                    text='海軍雷達站',
                    actions=[
                        PostbackTemplateAction(
                            label='駐地：全台各地',
                            data='這是ID=2'
                        ),
                        MessageAction(
                            label='詳細說明',
                            text='%海偵'
                        ),
                        URITemplateAction(
                            label='前往網頁',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30029&AID=30054'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2021/12/26/realtime/14886452.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=800&exp=3600&w=930&nt=1',
                    title='海軍海鋒大隊',
                    text='海軍飛彈部隊',
                    actions=[
                        PostbackTemplateAction(
                            label='駐地：全台各地',
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
                    thumbnail_image_url='https://imgur.com/a/zwMXGTk',
                    title=' 海軍教育訓練暨準則發展指揮部',
                    text='海軍新兵訓練中心、海軍技術學校/n海軍陸戰隊新兵訓練中心、海軍陸戰隊學校',
                    actions=[
                        PostbackTemplateAction(
                            label='駐地：左營、龍泉',
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
                    thumbnail_image_url='https://navy.mnd.gov.tw/Photo/OtherHTML/201610261134_976298.jpg',
                    title='海軍反潛航空大隊',
                    text='S-70C反潛直升機、500MD反潛直昇機',
                    actions=[
                        PostbackTemplateAction(
                            label='駐地：左營',
                            data='這是ID=2'
                        ),
                        MessageAction(
                            label='詳細說明',
                            text='%反潛'
                        ),
                        URITemplateAction(
                            label='前往網頁',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30029&AID=30057'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.6435-9/126933144_1746128488898865_1472026323777596786_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=8bfeb9&_nc_ohc=ufSob08X-pkAX_x7kDe&_nc_ht=scontent.fkhh1-1.fna&oh=00_AT8K51NCTW9jyHCVlP1DJnAUQufMhV9356ZupivPXlxoqg&oe=624FDFD3',
                    title='海軍海洋監偵指揮部',
                    text='海軍雷達站',
                    actions=[
                        PostbackTemplateAction(
                            label='駐地：全台各地',
                            data='這是ID=2'
                        ),
                        MessageAction(
                            label='詳細說明',
                            text='%海偵'
                        ),
                        URITemplateAction(
                            label='前往網頁',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30029&AID=30054'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2021/12/26/realtime/14886452.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=800&exp=3600&w=930&nt=1',
                    title='海軍海鋒大隊',
                    text='海軍飛彈部隊',
                    actions=[
                        PostbackTemplateAction(
                            label='駐地：全台各地',
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


#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)
def image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='圖片旋轉木馬',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://drive.google.com/file/d/1NzmAMTnsLVI7w2r0R-gK1I6Xq2ebIPvv/view?usp=sharing",
                    action=URITemplateAction(
                        label="2022形象影片",
                        uri="https://www.youtube.com/watch?v=SmeYkoJwL3A"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QOcAvjt.jpg",
                    action=URITemplateAction(
                        label="新鮮蔬菜",
                        uri="https://cdn.101mediaimage.com/img/file/1410464751urhp5.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/Np7eFyj.jpg",
                    action=URITemplateAction(
                        label="可愛狗狗",
                        uri="http://imgm.cnmo-img.com.cn/appimg/screenpic/big/674/673928.JPG"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QRIa5Dz.jpg",
                    action=URITemplateAction(
                        label="可愛貓咪",
                        uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                )
            ]
        )
    )
    return message




#關於LINEBOT聊天內容範例
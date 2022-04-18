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
                    label="我要認識海軍",
                    text="認識海軍"
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

def buttons_message3():
    message = TemplateSendMessage(
        alt_text='海軍官網',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i.imgur.com/l6tGJCx.png",
            title="🇹🇼中華民國海軍官方網站🇹🇼",
            text="還用問嗎？通通加就對了！",
            actions=[
                URITemplateAction(
                    label="海軍官方網站",
                    uri='https://navy.mnd.gov.tw/index.aspx'
                ),
                URITemplateAction(
                    label="海軍Fackbook",
                    uri='https://www.facebook.com/ROCNAVY.tw'
                ),
                URITemplateAction(
                    label="海軍Instagram",
                    uri='https://www.instagram.com/r.o.c.navy/'
                )
            ]
        )
    )
    return message

def buttons_message4():
    message = TemplateSendMessage(
        alt_text='海軍各式簡報',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i.imgur.com/9su5voz.png",
            title="🇹🇼海軍招募簡報🇹🇼",
            text="點選簡報了解海軍！",
            actions=[
                URITemplateAction(
                    label="海軍軍種單位簡介-長版",
                    uri='https://docs.google.com/presentation/d/e/2PACX-1vST9fKhfrl2wJIMPHw2eSlGLhAPw5R1S2l6Q9AKBehLFzFV7LO6M4y7zGi4sM9vyg/pub?start=true&loop=false&delayms=60000'
                )
            ]
        )
    )
    return message



#TemplateSendMessage - ConfirmTemplate(確認介面訊息)
def Confirm_Template():

    message = TemplateSendMessage(
        alt_text='你要找海軍招募員兼程式小編嗎？',
        template=ConfirmTemplate(
            text="你要找海軍最帥招募員兼小編嗎？",
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
                    thumbnail_image_url='https://scontent.ftpe3-1.fna.fbcdn.net/v/t39.30808-6/241519169_1970387399806305_3122669426780150672_n.jpg?_nc_cat=111&ccb=1-5&_nc_sid=8bfeb9&_nc_ohc=13R-vVhSg54AX83tdtF&_nc_ht=scontent.ftpe3-1.fna&oh=00_AT9lStYDpwOT9OGbCAejY5ynWBvEprl0W5uOquOjlN4hBg&oe=6257EF14',
                    title='陸戰九九旅',
                    text='鐵軍：鋼鐵勁旅，防衛固守，有如銅牆鐵壁之堅強勁旅',
                    actions=[
                        PostbackTemplateAction(
                            label='駐地：林園',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                         MessageAction(
                            label='詳細說明',
                            text='%99'
                        ),    
                        URITemplateAction(
                            label='了解陸戰九九旅',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30151&AID=30329'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://scontent.ftpe3-2.fna.fbcdn.net/v/t1.6435-9/137565444_1789654437879603_1663324744227075487_n.jpg?_nc_cat=102&ccb=1-5&_nc_sid=8bfeb9&_nc_ohc=Qdvp7-IBsFIAX9n38Mz&_nc_oc=AQlqH4-dGiX3y_hHseAsFYt5bzTIQDy1vFSwHCnA3TPXKsJVZlKtS3as8Px7-6StK_8&_nc_ht=scontent.ftpe3-2.fna&oh=00_AT9rtbE17t2_kpt3eAfJLctbqWqZz70CzL5xrS-AuFm0dQ&oe=6278F1FD',
                    title='陸戰六六旅',
                    text='先鋒：為陸戰隊先鋒，身先士卒，勇猛向前。',
                    actions=[
                        PostbackTemplateAction(
                            label='駐地：林口',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                         MessageAction(
                            label='詳細說明',
                            text='%66'
                        ),    
                        URITemplateAction(
                            label='了解陸戰六六旅',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30151&AID=30328'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://scontent.ftpe3-1.fna.fbcdn.net/v/t39.30808-6/270089018_2055861934592184_3550641929738566681_n.jpg?_nc_cat=111&ccb=1-5&_nc_sid=8bfeb9&_nc_ohc=meNODNqDhB0AX93LLFg&_nc_ht=scontent.ftpe3-1.fna&oh=00_AT_kiVcgiF3deBSGgIt1TNDsSNu6ArAposFpbYxKII8BDw&oe=625998CD',
                    title='登陸戰車大隊',
                    text='使命必達，送你抵達全世界每一個海灘',
                    actions=[
                        PostbackTemplateAction(
                            label='駐地：左營',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                         MessageAction(
                            label='詳細說明',
                            text='%登車'
                        ),    
                        URITemplateAction(
                            label='了解登陸戰車大隊',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30151&AID=30334'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://scontent.ftpe3-2.fna.fbcdn.net/v/t1.6435-9/45172095_2015223051856846_8514639047887421440_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=730e14&_nc_ohc=lpyWCbUs2GMAX84BpFW&_nc_ht=scontent.ftpe3-2.fna&oh=00_AT-wwj-DKGndBThLD1ru5kAPd5knd7Xs_4-2LX6Xp0cjrQ&oe=627B2FFA',
                    title='戰鬥支援大隊',
                    text='支援作戰，捨我其誰',
                    actions=[
                        PostbackTemplateAction(
                            label='駐地：左營',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                         MessageAction(
                            label='詳細說明',
                            text='%戰支'
                        ),    
                        URITemplateAction(
                            label='了解戰鬥支援大隊',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30151&AID=30335'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://scontent.ftpe3-2.fna.fbcdn.net/v/t1.6435-9/55560596_2216608638384952_1125144525174472704_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_ohc=1A9oy56uebsAX9eW1gx&_nc_ht=scontent.ftpe3-2.fna&oh=00_AT8PV5yBBn-pFmnyxxAxjlXlC8UgeeBPa0CcjUZ_bt_aKw&oe=627A96FA',
                    title='烏坵守備大隊',
                    text='同島一心，永保烏坵',
                    actions=[
                        PostbackTemplateAction(
                            label='駐地：烏坵',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                         MessageAction(
                            label='詳細說明',
                            text='%烏坵'
                        ),    
                        URITemplateAction(
                            label='了解烏坵守備大隊',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30151&AID=30332'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://media.nownews.com/nn_media/thumbnail/2021/01/1610253640473-95998eaff73245f1b416d187e5e47798-800x533.jpg?unShow=false',
                    title='兩棲偵搜大隊',
                    text='特種作戰，臨陣當先',
                    actions=[
                        PostbackTemplateAction(
                            label='駐地：左營',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                         MessageAction(
                            label='詳細說明',
                            text='%兩棲偵搜'
                        ),    
                        URITemplateAction(
                            label='了解兩棲偵搜大隊',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30151&AID=30333'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://scontent.ftpe3-1.fna.fbcdn.net/v/t1.6435-9/208936039_1920807614764284_53273476448588147_n.jpg?_nc_cat=104&ccb=1-5&_nc_sid=8bfeb9&_nc_ohc=nEwQzP-NfqgAX8Rh_nb&_nc_ht=scontent.ftpe3-1.fna&oh=00_AT9JOjCWBjpxBC_dvEDvFjjGSVuztd-Np8QmRA1cTmhiKw&oe=627AE692',
                    title='防空警衛群',
                    text='鐵衛：負責海軍重要軍事設施、港口及要塞守衛任務，誓死守衛。',
                    actions=[
                        PostbackTemplateAction(
                            label='基隆、台北、蘇澳、高雄、馬公',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                         MessageAction(
                            label='詳細說明',
                            text='%防警'
                        ),    
                        URITemplateAction(
                            label='了解防空警衛群',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30151&AID=30331'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://scontent.ftpe3-2.fna.fbcdn.net/v/t39.30808-6/240529550_1964941920350853_4804579489274630620_n.jpg?_nc_cat=107&ccb=1-5&_nc_sid=8bfeb9&_nc_ohc=Sla51cobEZIAX-kw8Vu&_nc_oc=AQke2uSY6glYUuDKjkXwirjOBzPX2Pi1QLppDQOJyQqWBIKitvH64WxZO8gsBIz4hpM&_nc_ht=scontent.ftpe3-2.fna&oh=00_AT8zcwJ69z8U4HeQaIYEugqAa78qQfsw69RSqmKPQxmR-Q&oe=6258282F',
                    title='三軍聯訓基地',
                    text='聯勇：負責國軍三軍聯合作戰演訓及實彈操演之任務，代名為聯勇。',
                    actions=[
                        PostbackTemplateAction(
                            label='駐地：恆春',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                         MessageAction(
                            label='詳細說明',
                            text='%三軍基地'
                        ),    
                        URITemplateAction(
                            label='了解三軍聯訓基地',
                            uri='https://navy.mnd.gov.tw/AboutUs/Partner_Info.aspx?ID=30151&AID=30331'
                        )
                    ]
                ),
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
                         MessageAction(
                            label='隊徽及照片',
                            text='%圖庫戰搜'
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
                    thumbnail_image_url='https://scontent.ftpe3-2.fna.fbcdn.net/v/t39.30808-6/277171938_2126818857496491_1956194813101538323_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=8bfeb9&_nc_ohc=1ZLvbquGrQIAX9QOtuX&_nc_ht=scontent.ftpe3-2.fna&oh=00_AT_UiTFHeF6yICYEpnwjzIwSUrouuZx8NQZjkBgigsTjRg&oe=6255BD08',
                    title=' 海軍教育訓練暨準則發展指揮部',
                    text='海軍新兵訓練中心、海軍技術學校\n海軍陸戰隊新兵訓練中心、海軍陸戰隊學校',
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
                    thumbnail_image_url='https://i.imgur.com/tg01yeu.jpg',
                    title='海軍保修指揮部',
                    text='左營後勤支援指揮部、蘇澳後勤支援指揮部\n基隆後勤支援指揮部、馬公後勤支援指揮部\n戰鬥系統工廠、補給總庫',
                    actions=[
                        PostbackTemplateAction(
                            label='駐地：左營、蘇澳、基隆、馬公',
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
                            label='駐地：台北、蘇澳、馬公、左營',
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
                            label='駐地：台北大直',
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
                    thumbnail_image_url='https://cnmoo.mnd.gov.tw/UploadFile/MainImg/MainImg_16162132.jpg',
                    title='大氣海洋局',
                    text='海軍版中央氣象台',
                    actions=[
                        PostbackTemplateAction(
                            label='駐地：高雄左營',
                            data='這是ID=2'
                        ),
                        MessageAction(
                            label='詳細說明',
                            text='%大氣'
                        ),
                        URITemplateAction(
                            label='前往網頁',
                            uri='https://cnmoo.mnd.gov.tw/'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://scontent.ftpe3-2.fna.fbcdn.net/v/t39.30808-6/276163906_2125863730925337_6027043035640067989_n.jpg?_nc_cat=107&ccb=1-5&_nc_sid=8bfeb9&_nc_ohc=3hRQRo4g8rIAX9Ih0vZ&_nc_ht=scontent.ftpe3-2.fna&oh=00_AT9uQFxzq3mn9f8qQ-YjoEwz-F-eDBUOwWO0-xu07Xjjqg&oe=6257DB1C',
                    title='海軍造船發展中心',
                    text='國艦國造戰力強',
                    actions=[
                        PostbackTemplateAction(
                            label='駐地：高雄左營',
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
                            label='駐地：高雄左營',
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
def image_carousel_message():
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
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/RbA7gnG.jpg",
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/A9NsmKb.jpg",
                ),
                 ImageCarouselColumn(
                    image_url="https://i.imgur.com/Qc9AcMt.jpg",
                ) ,
            ]
        )
    )
    return message



#關於LINEBOT聊天內容範例
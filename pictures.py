#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

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
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/RbA7gnG.jpg",
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/A9NsmKb.jpg",
                )
                 ImageCarouselColumn(
                    image_url="https://i.imgur.com/Qc9AcMt.jpg",
                )               
            ]
        )
    )
    return message
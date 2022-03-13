#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def test():
    message = TemplateSendMessage(
        alt_text='影片欣賞',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://static.wixstatic.com/media/f96bc7_b07e21aa4316452a8d135e6d9d5a331a~mv2.png/v1/fill/w_713,h_398,al_c,q_85,usm_0.66_1.00_0.01/2022%E6%B5%B7%E8%BB%8D%E5%BD%A2%E8%B1%A1%E5%BD%B1%E7%89%87%E5%B0%81%E9%9D%A2.webp",
                    action=URITemplateAction(
                        label="2022形象影片",
                        uri="https://www.youtube.com/watch?v=SmeYkoJwL3A"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://static.wixstatic.com/media/f96bc7_cca001d9b32842fa954f853e43893802~mv2.jpg/v1/fill/w_480,h_304,al_c,q_80,usm_0.66_1.00_0.01/152404222320711.webp",
                    action=URITemplateAction(
                        label="守護家園",
                        uri="https://www.youtube.com/watch?v=PycUw2oflaY"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://static.wixstatic.com/media/f96bc7_997399d1ed7249a4a32490b60a003b0c~mv2.png/v1/fill/w_480,h_269,al_c,q_85,usm_0.66_1.00_0.01/%E6%9C%AA%E5%91%BD%E5%90%8D.webp",
                    action=URITemplateAction(
                        label="海軍陸戰隊-英雄夢",
                        uri="https://www.youtube.com/watch?v=uXJin6jdpeE"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://static.wixstatic.com/media/f96bc7_c09d8f379c8d4fea822fa99a4cc465d0~mv2.png/v1/fill/w_480,h_259,al_c,q_85,usm_0.66_1.00_0.01/%E6%9C%AA%E5%91%BD%E5%90%8D.webp",
                    action=URITemplateAction(
                        label="惡名昭彰 feat.館長",
                        uri="https://www.youtube.com/watch?v=meFWwLI7glY"
                    )
                )
            ]
        )
    )
    return message
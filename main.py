from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    FlexMessage,
    FlexContainer
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)
import json
import os
from getScoreInfo import get_Info
from googlesheet import *
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
CHANNEL_SECRET = os.environ.get('CHANNEL_SECRET')

configuration = Configuration(access_token=ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


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
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    nba_teams = ["老鷹", "賽爾提克", "籃網", "黃蜂", "公牛", "騎士", "獨行俠", "金塊", "活塞", "勇士",
    "火箭", "溜馬", "快艇", "湖人", "灰熊", "熱火", "公鹿", "灰狼", "鵜鶘", "尼克", "雷霆",
    "魔術", "76人", "太陽", "拓荒者", "國王", "馬刺", "暴龍", "爵士", "巫師"]
    
    message = event.message.text
    
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        if message == '今日戰績':
            teams_data = json.load(open('json/teamFlex.json','r',encoding='utf-8'))
            flex_message_json = json.dumps(teams_data) 
            return_message = FlexMessage(alt_text="選擇球隊", contents=FlexContainer.from_json(flex_message_json))
        elif message in nba_teams:
            game_info = get_Info(message)
            flex_message_json = json.dumps(game_info) 
            return_message = FlexMessage(alt_text="比賽結果", contents=FlexContainer.from_json(flex_message_json))
        else:
            if '+' in message:
                money = message[1:]
                return_message = TextMessage(text=earn(int(money)))
            elif '-' in message:
                money = message[1:]
                return_message = TextMessage(text=loss(int(money)))
            elif message == '盈餘':
                return_message = TextMessage(text=total())
            else:
                return_message = TextMessage(text="請輸入正確的指令")
        
        line_bot_api.reply_message(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[return_message]
            )
        )
        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
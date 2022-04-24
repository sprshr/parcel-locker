import requests

telegramURL = "https://api.telegram.org/bot{token}/{method}"

class Bot():
    def __init__(self, APItoken:str):
        self.token = APItoken

    def send_message(self, chatID:str, message:str):
        pload = {
            'chat_id' : chatID,
            'text' : message,
            'parse_mode' : "HTML"
        }
        r = requests.post(telegramURL.format(token = self.token, method = "sendMessage"), data = pload)

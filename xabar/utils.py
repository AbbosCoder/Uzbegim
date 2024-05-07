import requests

def send_telegram_message(message):
    chat_id = '762725479'
    bot_token = "6489684054:AAFORCb7h_FJZmi8bETbO-wyvE-oEpO4iis"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'html',
    }
    response = requests.post(url, data=data)
    return response.status_code, response.json()

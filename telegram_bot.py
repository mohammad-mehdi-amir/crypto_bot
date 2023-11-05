
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler, Updater
from telegram.ext import CommandHandler

import requests
import json

API_URL='http://127.0.0.1:5000/'


def start(update, context):
    print(f'<{update.message.chat.username}> start the bot')
    buttons = [
        [InlineKeyboardButton('BTC 💵', callback_data='btc'),
         InlineKeyboardButton('ETH 💵', callback_data='eth')],
        [InlineKeyboardButton('USDT 💵', callback_data='usdt'),
         InlineKeyboardButton('DOGE 💵', callback_data='doge')],
        [InlineKeyboardButton('BNB 💵', callback_data='BNB'),
         InlineKeyboardButton('XRP 💵', callback_data='xrp')]
    ]
    update.message.reply_text(
        'Please select a cryptocurrency 👇🏻:',
        reply_markup=InlineKeyboardMarkup(buttons)
    )

def find_price(name):
    try:
        response = requests.get(API_URL)
        code=response.status_code
        print(response.status_code)
        dict1=response.json()

        for key,val in dict1.items():
            if key==name:
                dateandtime=dict1['time'].split(" ")
                string=f'Crypto name: {val["name"]} 💰\nPrice: {val["price"]} ＄\nRate:{val["rate"]}🏅\nDate: {dateandtime[0]} 📅\nTime: {dateandtime[1][:7]} ⏰\n\n    /start'
        return string
        
    except Exception as e:
        print(e)
        return 'something went wrong...\nplease try again.\n\n    /start'
    
def button(update, context):
    query = update.callback_query
    symbol = query.data

    if symbol == 'btc':
        message = find_price('BTC')
    elif symbol == 'eth':
        message = find_price('ETH')
    elif symbol == 'usdt':
        message = find_price('USDT')
    elif symbol == 'doge':
        message = find_price('DOGE')
    elif symbol == 'BNB':
        message = find_price('BNB')
    elif symbol == 'xrp':
        message = find_price('XRP')

    query.message.edit_text(message)

if __name__ == '__main__':
    token = "5869189918:AAEbx2d8yFGgvrHO70WfiXv5jccToaYpC5w"
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()

    updater.idle()

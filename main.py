from itranslate import itranslate as itrans
from telebot import types
import telebot
import os
import gtts
# https://t.me/new_bot_t_bot
bot=telebot.TeleBot('5870590773:AAEeJuLLMGWucFPMPz0XaM7k0zhTP_qpZf8')
lang={
    'ru': 'russia',
    'en': 'еnglish',
    "de": 'german',
    'ja': 'japanese'
}

@bot.message_handler(commands='start')
def send_start(message):
    markup= types.ReplyKeyboardMarkup(resize_keyboard=True)
    russia = types.KeyboardButton("Русский")
    еnglish = types.KeyboardButton("Английский")
    german = types.KeyboardButton("Немецкий")
    japanese = types.KeyboardButton("Японский")
    markup.add(russia, еnglish, german, japanese)
    bot.send_message(message.chat.id, 'Привет, я бот переводчик выберете язык', reply_markup=markup)
    print("test1")

@bot.message_handler(content_types ='text')
def do_translate(message):
    transed = itrans(message.text, to_lang=lang)
    print('test2')
     
    voice= gtts.gTTS(transed)# делаем звуковую дорожку 
    voice.save(transed+'.mp3')# сохр дорожку 
    bot.reply_to(message, transed)#  сохроняем 
    bot.send_audio(message.chat.id, audio=open (transed+".mp3","rb")) #отправка текста и звука
    os.remove(transed+'.mp3')# удаляем все 
    print('test3')

if __name__ ==  "__main__":
    try:
        bot.polling(non_stop=True)
    except Exception as e:
        print('Erorr'+ str(e))


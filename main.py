import telebot
from yt_dlp import YoutubeDL
import os
Sizning tokeningiz bilan tayyorlandi
API_TOKEN = '8353974376:AAE6BNJPB5emOwTAb10GnR5itJypK01QM00'
bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
bot.reply_to(message, "Salom! YouTube link yuboring, yuklab beraman.")
@bot.message_handler(func=lambda m: True)
def download_video(message):
url = message.text
if "youtube" in url or "youtu.be" in url:
msg = bot.reply_to(message, "Yuklanmoqda...")
try:
ydl_opts = {'format': 'best', 'outtmpl': 'v.mp4', 'quiet': True}
with YoutubeDL(ydl_opts) as ydl:
ydl.download([url])
with open('v.mp4', 'rb') as v:
bot.send_video(message.chat.id, v)
os.remove('v.mp4')
bot.delete_message(message.chat.id, msg.message_id)
except Exception as e:
bot.reply_to(message, f"Xatolik: {e}")
else:
bot.reply_to(message, "Bu YouTube linki emas!")
if name == "main":
bot.polling(none_stop=True)

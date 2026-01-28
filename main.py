import telebot
from yt_dlp import YoutubeDL
import os
API_TOKEN = '8353974376:AAE6BNJPB5emOwTAb10GnR5itJypK01QM00'
bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
bot.reply_to(message, "Salom! Link yuboring, yuklab beraman.")
@bot.message_handler(func=lambda m: True)
def download_video(message):
url = message.text
msg = bot.reply_to(message, "Yuklanmoqda...")
try:
ydl_opts = {
'format': 'best',
'outtmpl': 'v.mp4',
'quiet': True,
'no_check_certificate': True
}
with YoutubeDL(ydl_opts) as ydl:
ydl.download([url])

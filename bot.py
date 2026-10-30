import os
import telebot

# يتم جلب التوكن تلقائياً من إعدادات منصة Render
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك يا ركان! تم تشغيل بوت التيليجرام بنجاح وبدون أي مشاكل.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"أرسلت لي: {message.text}")

print("Bot is running...")
bot.infinity_polling()

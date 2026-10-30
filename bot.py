import os
import telebot

TOKEN = "9208941761:AAHYL9tqfPWyRNeN7c3DE0c0ClwMlFXrNyw"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "بنجاح وبدون أي مشاكل")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"أرسلت لي: {message.text}")

print("Bot is running...")
bot.infinity_polling()

import telebot

TOKEN = "9015170155:AAEyAXm81IRqIhiEUhbDAx_7M1s_jp0Y-D0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك يا ركان! البوت يعمل الآن بنجاح.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"أرسلت لي: {message.text}")

print("Bot is running...")
bot.infinity_polling()

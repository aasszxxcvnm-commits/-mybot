import telebot

TOKEN = "9015170155:AAEyAXm81IRqIhiEUhbDAx_7M1s_jp0Y-D0"
bot = telebot.TeleBot(TOKEN)

# رد على أمر /start فقط بدون تكرار للرسائل العادية
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك يا ركان! البوت يعمل الآن في المجموعة بنجاح وجاهز لأوامرك.")

# إذا ما تبيه يرد نهائياً على الرسائل العادية ويقعد صامت إلا لو ناديته، احذف أو علّق الدالة اللي تحت:
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     pass

print("Bot is running...")
bot.infinity_polling()

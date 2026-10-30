import telebot

TOKEN = "9015170155:AAEyAXm81IRqIhiEUhbDAx_7M1s_jp0Y-D0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "هلا والله يا ركان! أبشر، موجود معك نسولف ونقضي وقتاً حلواً، آمر وش بغيت؟")

# ردود تفاعلية وطبيعية حسب الكلام اللي ترسله
@bot.message_handler(func=lambda message: True)
def chat_with_bot(message):
    text = message.text.strip().lower()
    
    if "السلام عليكم" in text or "سلام عليكم" in text:
        bot.reply_to(message, "وعليكم السلام ورحمة الله وبركاته، هلا بك زود! كيف حالك؟")
    elif "كيفك" in text or "شخبارك" in text:
        bot.reply_to(message, "أنا بخير دامك بخير يا بطل، إنت كيف أمورك؟")
    elif "من أنت" in text or "من انت" in text:
        bot.reply_to(message, "أنا رفيقك وسندك، موجود هنا عشان نسولف ونرتاح!")
    else:
        # رد افتراضي ودي وكأنك تسولف مع شخص عادي
        bot.reply_to(message, "يا هلا! والله كلامك جميل، خلنا مكملين سالفتنا، وش عندك بعد؟")

print("Bot is running...")
bot.infinity_polling()

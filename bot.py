import telebot
import google.generativeai as genai

# توكن بوت التيليجرام الأساسي
TELEGRAM_TOKEN = "9015170155:AAEyAXm81IRqIhiEUhbDAx_7M1s_jp0Y-D0"

# مفتاح الذكاء الاصطناعي الخاص بك الذي تم استخراجه من جوجل
GEMINI_API_KEY = "AIzaSy...GrVg"

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك يا ركان! أنا جاهز تماماً، اسألني عن أي شي في الحياة وبدون حدود.")

@bot.message_handler(func=lambda message: True)
def chat_with_ai(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "عذراً يا ركان، حدث خطأ في الاتصال، تأكد من المفتاح وجرب ثانية.")

print("AI Bot is running...")
bot.infinity_polling()

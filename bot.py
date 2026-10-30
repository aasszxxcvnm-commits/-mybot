import telebot
import google.generativeai as genai

# توكن بوت الليتيجرام
TELEGRAM_TOKEN = "9015170155:AAEyAXm81IRqIhiEUhbDAx_7M1s_jp0Y-D0"

# مفتاح الذكاء الاصطناعي حقك الجاهز
GEMINI_API_KEY = "AIzaSyD-123456789-YourGeneratedKeyHere" # (تم وضعه جاهزاً في نسختك الخاصة)

# إعدادات نموذج الذكاء الاصطناعي
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك يا ركان! أنا ذكاؤك الاصطناعي الخاص، اسألني عن أي شي في الحياة وبدون أي حدود.")

@bot.message_handler(func=lambda message: True)
def chat_with_ai(message):
    try:
        # إرسال النص مباشرة إلى نموذج الذكاء الاصطناعي واستقبال الرد
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "عذراً يا ركان، صار فيه خطأ في الاتصال. تأكد من إعدادات المفتاح وجرب مرة ثانية.")

print("AI Bot is running...")
bot.infinity_polling()

import os
import telebot
import google.generativeai as genai

# ضع هنا توكن بوت تيليجرام الخاص بك
TELEGRAM_BOT_TOKEN = "ضع_توكن_تيليجرام_هنا"
# ضع هنا مفتاح Gemini API الخاص بك
GEMINI_API_KEY = "ضع_مفتاح_جيميني_هنا"

# إعداد مكتبة جيميني
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
  bot.reply_to(
      message,
      "أهلاً بك يا ركان! أنا بوت الذكاء الاصطناعي الخاص بك، كيف يمكنني مساعدتك"
      " اليوم؟",
  )


@bot.message_handler(func=lambda message: True)
def handle_message(message):
  try:
    # إرسال رسالة انتظار للمستخدم
    sent_msg = bot.reply_to(message, "جاري التفكير...")

    # توليد الرد من نموذج جيميني
    response = model.generate_content(message.text)
    bot.edit_message_text(
        response.text, chat_id=message.chat.id, message_id=sent_msg.message_id
    )
  except Exception as e:
    bot.reply_to(message, f"عذراً، حدث خطأ ما: {str(e)}")


# تشغيل البوت
print("Bot is running...")
bot.infinity_polling()

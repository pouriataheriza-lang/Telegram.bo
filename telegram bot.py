import telebot

TOKEN = "8348905025:AAFEKPajI6eDuWhpAPvFb6Bywq3lbmBVH7I"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! رضا ، ربات فعاله 😊")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.chat.id, "گفتی: " + message.text)

bot.infinity_polling()
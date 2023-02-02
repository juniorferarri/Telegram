import telebot
import time

token = '5953977982:AAGR-RNdU2QgnPqOhOy59xQw8Lz1cEjQBCI5953977982:AAGR-RNdU2QgnPqOhOy59xQw8Lz1cEjQBCI'

bot = telebot.TeleBot(token)


# Обработчик для команды start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот для QPython. Что ты хочешь сделать? /help')    


# Обработчик для команды help
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я могу помочь тебе со следующими вещами: \n /mute - Выдать мут на время с причиной \n /ban - Банить с причиной на время \n /unmute - Снять мут \n /unban - Снять бан')    

# Обработчик для команды mute
@bot.message_handler(commands=['mute'])
def start_message(message):
    bot.send_message(message.chat.id, 'Кому нужно выдать мут?')

# Обработчик для команды ban
@bot.message_handler(commands=['ban'])
def start_message(message):
    bot.send_message(message.chat.id, 'Кого нужно забанить?')

# Обработчик для команды unmute
@bot.message_handler(commands=['unmute'])
def start_message(message):
    bot.send_message(message.chat.id, 'Кому нужно снять мут?')

# Обработчик для команды unban
@bot.message_handler(commands=['unban'])
def start_message(message):
    bot.send_message(message.chat.id, 'Кого нужно разбанить?')

# Запускаем бота
bot.polling(none_stop=True)
import telebot  # pyTelegramBotAPI 4.3.1
from telebot import types
from io import BytesIO
import imgbb


bot = telebot.TeleBot('5150353309:AAHW1DPdYWBmnLyYFHFmmFJpZPstV1wuwGo')  # Создаем экземпляр бота @Salakhov_Shamil_1MD25_bot

# -----------------------------------------------------------------------
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def command(message, res=False):
    chat_id = message.chat.id
    txt_message = f"Здравствуй, {message.from_user.first_name}, я твой преподаватель! Отправь фото своего дз."
    bot.send_message(message.chat.id, text=txt_message)

    
# -----------------------------------------------------------------------
# Получение фото от юзера
@bot.message_handler(content_types=['photo'])
def get_messages(message):
    chat_id = message.chat.id
    username = message.from_user.first_name + ' ' + message.from_user.last_name

    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_name = message.photo[0].file_id + '.jpeg'

    src = 'Z:/Алгоритмизация и программирование/1-МД-25/Салахов/test/' + file_name
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)

    imgbb.photo_to_excel(username, src)
    bot.reply_to(message, "Спасибо, получил твое ДЗ. К концу недели будет проверено!")


# ---------------------------------------------------------------------


bot.polling(none_stop=True, interval=0)  # Запускаем бота
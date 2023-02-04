import telebot
from telebot import types

bot = telebot.TeleBot("5679649195:AAGhGUtb268wOoef4bYGr2BlMc54LZX9gv8")


def start_markup():
    markup = types.InlineKeyboardMarkup(row_width=True)
    link_keyboard1 = types.InlineKeyboardButton(text="⚠️подпишись⚠️", url="https://t.me/animeavg")
    link_keyboard2 = types.InlineKeyboardButton(text="⚠️подпишись⚠️", url="https://t.me/viizzifilm")
    link_keyboard3 = types.InlineKeyboardButton(text="⚠️подпишись⚠️", url="https://t.me/hgyfythv")
    check_keyboard = types.InlineKeyboardButton(text="✅проверить✅",callback_data="check")
    markup.add(link_keyboard1,link_keyboard2,link_keyboard3,check_keyboard)
    return markup

def start_markup1():
    markup = types.InlineKeyboardMarkup(row_width=True)
    link_keyboard1 = types.InlineKeyboardButton(text="🎎вот канал🎎", url="https://t.me/+6-M0clfJ3kFjMTBk")
    markup.add(link_keyboard1)
    return markup


@bot.message_handler(commands=["start"])
def start(message):
    photo = open('anime_hai.png', 'rb')
    chat_id = message.chat.id
    first_name = message.chat.first_name
    bot.send_photo(chat_id, photo, f"хай {first_name} !\n"
                                   f"Чтобы получить аниме тебе надо сделать задание потписатся на канали", reply_markup=start_markup())


def check(call):
    status = ['creator', 'administrator', 'member']
    for i in status:
        if i == bot.get_chat_member(chat_id="-1001474093598", user_id=call.message.chat.id).status:
            check2(call)
            break

    else:
        photo2 = open('i.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo2, "⚠️Тебе надо подписаться чтобы получить аниме⚠️", reply_markup=start_markup())


def check2(call):
    status = ['creator', 'administrator', 'member']
    for i in status:
        if i == bot.get_chat_member(chat_id="-1001633184989", user_id=call.message.chat.id).status:
            check3(call)
            break

    else:
        photo2 = open('i.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo2, "⚠️Тебе надо подписаться чтобы получить аниме⚠️", reply_markup=start_markup())


def check3(call):
    status = ['creator', 'administrator', 'member']
    for i in status:
        if i == bot.get_chat_member(chat_id="-1001863513401", user_id=call.message.chat.id).status:
            photo1 = open('anime1.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo1, "Ну вот ты все сделал спс теперь ты можешь смотреть аниме🎎",reply_markup=start_markup1())
            break

    else:
        photo2 = open('i.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo2, "⚠️Тебе надо подписаться чтобы получить аниме⚠️", reply_markup=start_markup())


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'check':
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
        check(call)


bot.polling(none_stop=True)
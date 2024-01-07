import telebot
import webbrowser
from telebot import types


bot = telebot.TeleBot('6808687019:AAHpcxKWXQm3_D8LNXNyj_rJYIRGv2wvNvs')


@bot.message_handler(commands=['start'])
def start1(message):
    user_id = message.from_user.id
    kb = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Send to demon lord😈')
    kb.row(btn1)
    btn2 = types.KeyboardButton('Delete')
    btn3 = types.KeyboardButton('Change')
    kb.add(btn2, btn3)
    file = open('./damn.jpg', 'rb')
    bot.send_photo(user_id, file, reply_markup=kb)
    # bot.reply_to(message, '!!?!?!', reply_markup=kb)
    bot.register_next_step_handler(message, click_on)


def click_on(message):
    user_id = message.fom_user.id
    if message.text == 'Send to demon lord':
        bot.send_message(user_id, 'He is already looking for ypu from abyss!')
    else:
        bot.send_message(user_id, 'Try resent to him!')

@bot.message_handler(commands=['xxxvideo'])
def xxxvideo(message):
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Hello bro!')


@bot.message_handler(commands=['help'])
def help(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Hello brooo!,\n'
                              'You need some help?'
                              '\n Never say help, say help me homis or'
                              ' text /help_me_homies')

@bot.message_handler(commands=['help_me_homies'])
def help_me_homies(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Ok bro i show what can this do!'
                              '\n First /start this command make this bot work <b>for</b> <em><u>you</u></em>\n'
                              'Second /xxxvideo throw you to very interest video\n'
                              'Third text "ID" and  stole your ID to show it to you',
                              parse_mode='html')


@bot.message_handler()
def empty(message):
    user_id = message.from_user.id
    if message.text.lower() == 'shit':
        bot.send_message(user_id, 'What happen bro?')
    elif message.text.lower() == 'id':
        bot.send_message(user_id, f'Oh i get it! What did you do? I found your ID in Pentagon database.'
                                  f' It is your ID:{user_id}')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    kb = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Send to demon lord', callback_data='send')
    kb.row(btn1)
    btn2 = types.InlineKeyboardButton(text='Delete', callback_data='delete')
    btn3 = types.InlineKeyboardButton(text='Change', callback_data='change')
    kb.add(btn2, btn3)
    bot.reply_to(message, 'Eeeuuuuwww!!?!?!', reply_markup=kb)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'change':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)



bot.polling(non_stop=True)






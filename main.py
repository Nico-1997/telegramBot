import telebot
from telebot import types


TOKEN = '7008205697:AAHTgqWIBKiuxxHNSMEzWq8IOH_PnbXOYqo'
bot = telebot.TeleBot(TOKEN)


#Creacion de comandos `/star` y `/help`

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hola nico, eres una tonta')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Chau')


# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# bot.reply_to(message, message.text)


@bot.message_handler(commands=['pizza'])
def send_options(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    #Botones
    btn_si = types.InlineKeyboardButton('si', callback_data='pizza_si')
    btn_no = types.InlineKeyboardButton('no', callback_data='pizza_no')


    #Agregando botones
    markup.add(btn_si, btn_no)
    

    #Enviar mensaje con los botones
    bot.send_message(message.chat.id, "te gusta la piza?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    if call.data == 'pizza_si':
        bot.answer_callback_query(call.id, 'a mi tambien me gusta')
    elif call.data == 'pizza_no':
        bot.answer_callback_query(call.id, 'a mi tampoco')


@bot.message_handler(commands=['hasbu'])
def send_imagge(message):
    img_url='https://media.tycsports.com/files/2022/06/04/436717/hasbulla-boca_862x485.webp?v=1'
    bot.send_photo(chat_id=message.chat.id, photo=img_url)




 
if __name__ == "__main__":
    bot.polling(none_stop=True)

from typing import Final
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, CallbackQueryHandler,CallbackContext,filters


Token: Final = '6571411673:AAEsrOjiRI-MQQxoGvx-3D2c0mqCp4lW62o'
Bot_username: Final = '@Translator_pe_bot'

async def select_language(update : Update , context : CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("Persian" , callback_data="Persian"),
            InlineKeyboardButton("Arabic" , callback_data="Arabic"),
            InlineKeyboardButton("Germany" , callback_data="Germany")
         ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("select your language" ,reply_markup= reply_markup)

async def reply(updat : Update , context : ContextTypes.DEFAULT_TYPE):
    user_input =updat.message.text
    await updat.message.reply_text(f'you say {user_input}')


async def button_menu(update : Update , context : CallbackContext):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=query.data)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} causded error {context.error}')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text  
    await update.message.reply_text(f'send me {text}')  

if __name__ == '__main__':
    app = Application.builder().token(Token).build()


    app.add_handler(CommandHandler('select_language', select_language))
    app.add_handler(MessageHandler(filters.TEXT, reply))
    app.add_handler(CallbackQueryHandler(button_menu))
    app.add_error_handler(error)
    print("polling")
    app.run_polling(poll_interval=3)
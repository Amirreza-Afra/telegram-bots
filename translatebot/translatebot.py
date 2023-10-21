from typing import Final
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, CallbackQueryHandler,CallbackContext,filters


Token: Final = '6571411673:AAEsrOjiRI-MQQxoGvx-3D2c0mqCp4lW62o'
Bot_username: Final = '@Translator_pe_bot'

async def select_menu(update : Update , context : CallbackContext):
    keyboard = {
        InlineKeyboardButton('hello' , callback_data="hello world")
    }
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("say hello!" ,reply_markup= reply_markup)


async def start_command(update: Update, context : ContextTypes.DEFAULT_TYPE):
    massage_user :str =update.message.chat.first_name + update.message.chat.last_name
    await update.message.reply_text(f"hi {massage_user}")


async def handle_massage(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message_type: str = update.message.chat.type
    text: str = update.message.text  

    await update.message.reply_text(f'send me {text}')  

if __name__ == '__main__':
    app = Application.builder().token(Token).build()


app.add_handler(CommandHandler('start', start_command))
app.add_handler(MessageHandler(filters.TEXT, handle_massage))
print("poling")
app.run_polling(poll_interval=4)

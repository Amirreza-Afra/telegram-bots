from typing import Final
from telegram import InlineKeyboardButton, Update, ReplyKeyboardMarkup, MenuButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler


Token: Final = '6571411673:AAEsrOjiRI-MQQxoGvx-3D2c0mqCp4lW62o'
Bot_username: Final = '@Translator_pe_bot'


async def start_command(update: Update, context : ContextTypes.DEFAULT_TYPE):
    massage_user :str =update.message.chat.first_name + update.message.chat.last_name
    await update.message.reply_text(f"hi {massage_user}")
    

if __name__ == '__main__':
    app = Application.builder().token(Token).build()


app.add_handler(CommandHandler('start', start_command))
print("poling")
app.run_polling(poll_interval=4)

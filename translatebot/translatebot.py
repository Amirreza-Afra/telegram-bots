from typing import Final
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, CallbackQueryHandler, CallbackContext, filters
from translate import Translator

Token: Final = '6571411673:AAEsrOjiRI-MQQxoGvx-3D2c0mqCp4lW62o'
Bot_username: Final = 'https://t.me/Translator_pe_bot'

lang = ""


async def select_language(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("Persian", callback_data="Persian"),
            InlineKeyboardButton("Arabic", callback_data="Arabic"),
            InlineKeyboardButton("Azerbaijani ", callback_data="Azerbaijani")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("select your language", reply_markup=reply_markup)




async def button_menu(update: Update, context: CallbackContext):
    global lang
    lang = update.callback_query.data.lower()
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f'{query.data} selected for translate')
    return query.data


def translat(input):
    translator = Translator(from_lang="english", to_lang=lang)
    translation = translator.translate(input)
    return translation


async def reply_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type == "group":
        MessageHandler(select_language)
        data = CallbackQueryHandler(button_menu)
        await update.message.reply_text(translat(data))
    else :
        return


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    await update.message.reply_text(translat(user_input))

def error(update, context):
    print(f"Update {update} caused error {context.error}")

if __name__ == '__main__':
    app = Application.builder().token(Token).build()

    app.add_handler(CommandHandler('start', select_language))
    app.add_handler(CommandHandler('select_language', select_language))
    app.add_handler(MessageHandler(filters.TEXT, reply))
    app.add_handler(CallbackQueryHandler(button_menu))
    app.add_error_handler(error)
    print("polling")
    app.run_polling(poll_interval=3)

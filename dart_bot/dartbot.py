from typing import Final
from telegram import InlineKeyboardButton, Update,ReplyKeyboardMarkup, MenuButton, CallbackQuery
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from finish import Finish

Token: Final = '6682953975:AAElZmf01phPegkD0cqed1dQ9oElWO6A8rA'
BOT_USERNAME: Final = '@Info_materbot'

finall = Finish()

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hi \U0001F970 chose option you want  or enter number between 2 and 170 to see how to finish")
    menu_data = {
        "Checkouts": "",
        "how to play dart ": "",
    }

    buttons = []
    for category, items in menu_data.items():
        if items:
            buttons.append(InlineKeyboardButton(category, callback_data=f"category:{category}"))
        else:
            buttons.append(InlineKeyboardButton(category))

    keyboard = ReplyKeyboardMarkup.from_column(buttons)
    await update.message.reply_text("Please select a category:", reply_markup=keyboard)



def first_handelr_response(txet: str) -> str:
     return finall.search_num(txet) 


async def handle_callback_query(update: Update, context:ContextTypes.DEFAULT_TYPE):
    callback_query: CallbackQuery = update.callback_query
    category = callback_query.data.split(":")[1]
    if category == "Checkouts":
                await callback_query.answer("enter a number between 2 and 170 to see finish of it")
    elif category == "Category 2":
              await callback_query.answer("Category 2 selected")
    
async def handle_massage(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'user ({update.message.chat.id}) in {message_type}: "{text}"')

    if "category" in context.user_data  == "Checkouts":
        
        chat_id = context.user_data["chat_id"]
        await context.bot.send_message(chat_id, f'Thank you for entering: "{text}"')

        del context.user_data["category"]
        del context.user_data["chat_id"]
    else:
        responses: str = first_handelr_response(text)
        print("bot:", responses )
        await update.message.reply_text(responses)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} causded error {context.error}')


if __name__ == '__main__':
    app = Application.builder().token(Token).build()

app.add_handler(CommandHandler('start', start_command))
app.add_handler(MessageHandler(filters.TEXT, handle_massage))
app.add_error_handler(error)
app.add_handler(CallbackQueryHandler(handle_callback_query))

print("polling")
app.run_polling(poll_interval=3)

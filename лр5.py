import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes


TOKEN = "7498956630:AAGkfpIqS4rsAuIPxvT-v8LkSU8vG44oA1I"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет сообщение с кнопками."""
    keyboard = [
        [
            InlineKeyboardButton("Кнопка 1", callback_data='button_1'),
            InlineKeyboardButton("Кнопка 2", callback_data='button_2'),
        ],
        [
            InlineKeyboardButton("Кнопка 3", callback_data='button_3')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Выберите действие:', reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обрабатывает нажатия кнопок."""
    query = update.callback_query
    await query.answer()  # Отправляет подтверждение нажатия

    button_data = query.data
    if button_data == 'button_1':
        await query.edit_message_text(text="Вы нажали кнопку 1!")
    elif button_data == 'button_2':
        await query.edit_message_text(text="Вы нажали кнопку 2!")
    elif button_data == 'button_3':
        await query.edit_message_text(text="Вы нажали кнопку 3!")
    else:
        await query.edit_message_text(text="Неизвестная кнопка!")


async def main() -> None:
    """Запускает бота."""
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    polling_started = False
    try:
        await application.run_polling()
        polling_started = True
    except Exception as e:
       logger.error(f"Error during polling: {e}")
    finally:
       if polling_started:
         await application.stop()
       await application.shutdown()


if __name__ == '__main__':
    asyncio.run(main())


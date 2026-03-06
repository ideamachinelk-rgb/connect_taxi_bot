import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Bot token is read from Railway environment variable
import os
TOKEN = os.environ.get("TOKEN")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🚕 Request Ride"],
        ["🚗 Driver Registration"]
    ]
    
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "🚕 Welcome to Connect Taxi\n\nChoose an option:",
        reply_markup=reply_markup
    )

# Handle basic messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🚕 Request Ride":
        await update.message.reply_text("📍 Please send your pickup location.")
    elif text == "🚗 Driver Registration":
        await update.message.reply_text("Please send your phone number to register as a driver.")
    else:
        await update.message.reply_text("❌ Invalid option. Tap /start to begin again.")

# Main function
async def main():
    if not TOKEN:
        print("ERROR: TOKEN is missing. Add it as an environment variable!")
        return

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("Bot running...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

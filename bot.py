import os
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Get token from Railway environment variable
TOKEN = os.environ.get("TOKEN")

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Start command
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

# Handle user messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🚕 Request Ride":
        await update.message.reply_text("📍 Please send your pickup location (or type an address).")

    elif text == "🚗 Driver Registration":
        await update.message.reply_text("📱 Please send your phone number to register as a driver.")

    else:
        await update.message.reply_text("❌ Unknown option. Please choose from the menu.")

# Main function
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()

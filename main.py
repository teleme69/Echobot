from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Flask app for keep-alive
app = Flask(__name__)

@app.route("/")
def home():
    return "The bot is alive!"

def run():
    app.run(host="0.0.0.0", port=8080)

# Telegram bot functions
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! I'm your bot. Send me any message, and I'll echo it back.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

def main():
    # Replace 'YOUR_BOT_TOKEN' with your Telegram bot token
    bot_token = '6980962954:AAG_hAi4fwNaxW0eARXkH4AxfRlO6i1u_DQ'

    # Create the Application
    application = Application.builder().token(bot_token).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the Flask server in a separate thread
    Thread(target=run).start()

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()

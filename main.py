from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Flask app for keep-alive
app = Flask(__name__)

@app.route("/")
def home():
    return "The bot is alive!"

def run():
    app.run(host="0.0.0.0", port=8080)

# Telegram bot functions
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I'm your bot. Send me any message, and I'll echo it back.")

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main():
    # Replace 'YOUR_BOT_TOKEN' with your Telegram bot token
    bot_token = '6980962954:AAG_hAi4fwNaxW0eARXkH4AxfRlO6i1u_DQ'
    updater = Updater(bot_token)

    # Register handlers
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the bot in a separate thread
    Thread(target=run).start()

    # Start polling
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

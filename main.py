"""
main.py

The main file where the bot handles incoming messages.
"""

# SECTION: Import modules

import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from decouple import config

import src.replies as REPLIES
import src.calendar as CALENDER
import src.analysis as ANALYSIS

# -----------------------
# SECTION: Initialisation
# -----------------------

# Get environment variables
API_TOKEN = config('API_TOKEN', cast=str)
DEBUG = config('DEBUG', default=False, cast=bool)
PORT = config('PORT', default=5000, cast=int)
WEBHOOK_DOMAIN = config('WEBHOOK_DOMAIN', cast=str)
WEBHOOK_URL = WEBHOOK_DOMAIN + API_TOKEN

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# ------------------
# SECTION: Bot logic
# ------------------

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
#
# Note:
# - context: callback context passed by telegram.ext.Handler/Dispatcher

def start(update, context):
    """Runs when the command /start is issued by the user.

    Args:
        update ([type]): [description]
        context ([type]): [description]
    """

    REPLY, PARSE_MODE = REPLIES.reply_start()
    context.bot.send_message(chat_id=update.effective_chat.id, text=REPLY, parse_mode=PARSE_MODE)

    msg_to_analyse = update.message.text

def help(update, context):
    """Runs when the command /help is issued by the user. This is a callback function that accepts the update and context objects

    Args:
        update ([type]): [description]
        context ([type]): [description]
    """

    REPLY, PARSE_MODE = REPLIES.reply_help()
    context.bot.send_message(chat_id=update.effective_chat.id, text=REPLY, parse_mode=PARSE_MODE)

def settings(update, context):
    """Handler to set bot settings"""

    """
    Might want to add in user preference for calendar format.
    - CSV: Google Calendar
    - ics/ical: iCalendar Open Format
    """
    pass

def echo(update, context):
    """Echo the user message."""
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    pass

def unknown_cmd(update, context):
    """Handle messages that are not commands"""

    REPLY, PARSE_MODE = REPLIES.reply_unknown()
    context.bot.send_message(chat_id=update.effective_chat.id, text=REPLY, parse_mode=PARSE_MODE)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

# -------------
# SECTION: Main
# -------------

# Set up the telegram bot


def main():
    """The entry point for the program. Sets up updaters, dispatchers, and handlers.
    """

    # --- Setting updater and dispatchers ---

    # Create the Updater and pass it your bot's token.
    # Note: Make sure to set use_context=True to use the new context-based callbacks. No longer necessary after v12 framework.
    updater = Updater(API_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # --- Registering Handlers ---

    # Add Telegram command handlers to respond to valid bot commands (those prefixed with "/")
    # The command handler accepts a "string", and a callback as well as an optional filter
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("settings", settings))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))
    
    # Handle msgs that are not commands
    dp.add_handler(MessageHandler(Filters.command, unknown_cmd))

    # log all errors
    dp.add_error_handler(error)

    # --- Start the Bot ---
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=API_TOKEN)
    updater.bot.setWebhook(WEBHOOK_URL)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
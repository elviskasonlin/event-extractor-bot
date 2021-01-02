"""
main.py

The main file where the bot handles incoming messages.
"""

# SECTION: Import modules

import logging
import os

# Telegram Wrapper Modules
import telegram.ext
import telegram
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Config decoupler
import decouple
# from decouple import config

# Source files
import src.replies as REPLIES
import src.calendar as CALENDER
import src.analysis as ANALYSIS

# -----------------------
# SECTION: Initialisation
# -----------------------

# Get environment variables
API_TOKEN = decouple.config('API_TOKEN', default="", cast=str)
DEBUG = decouple.config('DEBUG', default=False, cast=bool)
PORT = decouple.config('PORT', default=5000, cast=int)
WEBHOOK_DOMAIN = decouple.config('WEBHOOK_DOMAIN', default="", cast=str)
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

def start(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    """Runs when the command /start is issued by the user.

    Args:
        * update (telegram.Update object): Object representing an incoming update
        * context (telegram.ext.CallbackContext object): Context object passed to the callback called by telegram.ext.Handler or by the telegram.ext.Dispatcher
    """

    REPLY, PARSE_MODE = REPLIES.reply_start()
    context.bot.send_message(chat_id=update.effective_chat.id, text=REPLY, parse_mode=PARSE_MODE)

    msg_to_analyse = update.message.text

def help(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    """Runs when the command /help is issued by the user. This is a callback function that accepts the update and context objects

    Args:
        * update (telegram.Update object): Object representing an incoming update
        * context (telegram.ext.CallbackContext object): Context object passed to the callback called by telegram.ext.Handler or by the telegram.ext.Dispatcher
    """

    REPLY, PARSE_MODE = REPLIES.reply_help()
    context.bot.send_message(chat_id=update.effective_chat.id, text=REPLY, parse_mode=PARSE_MODE)

def settings(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    """Handler to set bot settings
    
    Args:
        * update (telegram.Update object): Object representing an incoming update
        * context (telegram.ext.CallbackContext object): Context object passed to the callback called by telegram.ext.Handler or by the telegram.ext.Dispatcher
    """

    """
    Might want to add in user preference for calendar format.
    - CSV: Google Calendar
    - ics/ical: iCalendar Open Format
    """
    pass

def echo(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    """Echos the user message. Currently not in use.
    
    Args:
        * update (telegram.Update object): Object representing an incoming update
        * context (telegram.ext.CallbackContext object): Context object passed to the callback called by telegram.ext.Handler or by the telegram.ext.Dispatcher
    """

    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    pass

def unknown_cmd(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    """Handle messages that are not commands
    
    Args:
        * update (telegram.Update object): Object representing an incoming update
        * context (telegram.ext.CallbackContext object): Context object passed to the callback called by telegram.ext.Handler or by the telegram.ext.Dispatcher
    """

    REPLY, PARSE_MODE = REPLIES.reply_unknown()
    context.bot.send_message(chat_id=update.effective_chat.id, text=REPLY, parse_mode=PARSE_MODE)

def error(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    """Log errors caused by Updates using the logging module
    
    Args:
        * update (telegram.Update object): Object representing an incoming update
        * context (telegram.ext.CallbackContext object): Context object passed to the callback called by telegram.ext.Handler or by the telegram.ext.Dispatcher
    """
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
    updater = telegram.ext.Updater(API_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # --- Registering Handlers ---

    # Add Telegram command handlers to respond to valid bot commands (those prefixed with "/")
    # The command handler accepts a "string", and a callback as well as an optional filter
    dp.add_handler(telegram.ext.CommandHandler("start", start))
    dp.add_handler(telegram.ext.CommandHandler("help", help))
    dp.add_handler(telegram.ext.CommandHandler("settings", settings))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))
    
    # Handle msgs that are not commands
    dp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.command, unknown_cmd))

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
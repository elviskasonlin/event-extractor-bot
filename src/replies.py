"""
replies.py

The default replies to bot commands
"""

from telegram import ParseMode

# NOTE
# For MarkdownV2 as a text format used in telegram bot api 4.5 onwards, the following characters much be escaped:
# - Inside (...) part of inline link definition, the following must be escaped with a preceding '\' character
#   - all ')' and '\'
# - In all other places, the following must be escaped with preceding character `\`:
#   - '_', '*', '[',
#   - ']', '(', ')',
#   - '~', '`', '>',
#   - '#', '+', '-',
#   - '=', '|', '{',
#   - '}', '.', '!',
# As such, ignore errors raised by a python linter for lines with this

def reply_start():
    """Returns the reply intended as a response to /start command

    Returns:
        reply (str): The standard reply for /start
        reply_type (obj): Type of reply to be provided as an argument when passed into telegram message handler
    """

    reply_type = ParseMode.MARKDOWN_V2
    reply = "Hi\! This bot extracts key event details from a given text message and returns a completed calendar entry in either icalendar or csv format"

    return reply, reply_type

def reply_help():
    """Returns the reply intended as a response to /help command
    
    Returns:
        reply (str): The standard reply for /help
        reply_type (obj): Type of reply to be provided as an argument when passed into telegram message handler
    """

    reply_type = ParseMode.MARKDOWN_V2
    reply = """
    *Help Section*
    1\. Type /start to start the bot
    2\. Type /settings to change bot settings
    3\. Type /help to show this menu again
    """
 
    return reply, reply_type

def reply_settings():
    """Returns the reply intended as a response to /settings command
    
    Returns:
        reply (str): The standard reply for /settings
        reply_type (obj): Type of reply to be provided as an argument when passed into telegram message handler
    """

    reply_type = ParseMode.MARKDOWN_V2
    reply = """
    *Settings*
    This bot does not offer any settings to customise at the moment
    """
 
    return reply, reply_type

def reply_unknown():
    """Returns the reply intended as a response to unknown commands
    
    Returns:
        reply (str): The standard reply for invalid commands
        reply_type (obj): Type of reply to be provided as an argument when passed into telegram message handler
    """

    reply_type = ParseMode.MARKDOWN_V2
    reply = """
    Sorry\, I do not understand your request\.
    Please type /help to learn more about available commands
    """
 
    return reply, reply_type
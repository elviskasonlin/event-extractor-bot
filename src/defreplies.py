"""
defreplies.py

The default replies to certain commands
"""

def reply_start():
    """Returns the reply intended as a response to /start command"""

    reply_type = "MarkdownV2"
    reply = "Hi\! This bot extracts key event details from a given text message and returns a completed calendar entry in either icalendar or csv format"

    return reply, reply_type

def reply_help():
    """Returns the reply intended as a response to /help command"""

    reply_type = "MarkdownV2"
    reply = """
    *Help Section*\ 1\) Type /start to start the bot \ 2\) Type /analyse followed by a space and your message to get your results straight away
    """
 
    return reply, reply_type

def reply_unknown():
    """Returns the reply intended as a response to unknown commands"""

    reply_type = "MarkdownV2"
    reply = """
    Sorry, I do not understand your request\. Please type /help to learn more about available commands.
    """
 
    return reply, reply_type



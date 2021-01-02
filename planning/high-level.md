# Activity

User intent: Help me identify key event details automantically and create a calendar entry 
Available options: /start /help /settings

# Flow

## 1. I want to create a calendar entry
1. Greeted by information regrading the bot's functionalities
2. Start the process
3. Paste message with event details for processing
4. Wait for processing
   1. If the message provided does not have sufficient information, I will be shown an error and asked to re-enter the message by pressing /start again
5. Download the calendar file (ical)
6. Add calendar entry to my personal calendar

## 2. I want to know about what the bot can do


# Potential Variations

- Direct calendar connection on the server with web front-end for direct addition to user's calendar (sign-in/sign-out configurable in settings)
- Saving of last few calendar entries for download (configurable in settings)

# Good-to-haves

- Able to be added into a chat group
- Inline hints
- Direct connection to user's google calendar
  - Privacy concerns
  - Trust concerns

# Requirements

- General command handling
- Processing function (major)
- Privacy Policy (bot)

# Resources

- [Using SQLite Database](https://www.codementor.io/@garethdwyer/building-a-chatbot-using-telegram-and-python-part-2-sqlite-databse-backend-m7o96jger?icn=post-goi5fncay&ici=post-m7o96jger)

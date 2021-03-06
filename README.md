# Event Extractor Telegram Bot
A telegram bot that extracts event details from a given event description and creates a calendar entry for the user.

Uses ```python-telegram-bot``` wrapper for telegram bot API and uses ```heroku``` to deploy.

More information can be found in /planning folder.
- High-level planning: /high-level.md
- Low-level planning: /low-level.md

## Setting up the environment

1. (Optional) Install ```pyenv``` to manage your python versions. Install ```virtualenv``` to enable python virtual environments.
2. Install ```pipenv``` to manage per-project dependencies and install the packages required by this project.
3. Run ```pipenv install``` to install all the dependencies to get the environment up and running
    3.1 Run ```pipenv install --dev``` to install dev dependencies like sphinx
4. Run ```pipenv shell``` to enter into the ```pipenv``` environment with all the dependencies initialised and installed

For any code changes, just push the code to the master branch on GitHub. Heroku will automatically build and deploy the new build to production.

## Remarks

* Double-check the environment variables (for Heroku, it's under "Settings > Config Vars")

## To-do

- [x] Set up handlers for the calender text entry and processing
- [] Set up available commands hint
- [] !! Add persistence with database and a custom class
- [] ! Add per-user settings
- [] !!! Analysis process
- [] !! Exporting to ical or csv
- [x] !! Draw a flow diagram
- [x] !!! Get familiarised with handlers and setting handlers
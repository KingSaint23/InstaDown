import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
    INSTA_USERNAME = os.environ.get('INSTA_USERNAME', None)
    INSTA_PASSWORD = os.environ.get('INSTA_PASSWORD', None)
else:
    # Fill the Values
    API_ID = 21672669
    API_HASH = "cf7a8a270b557e4bbdda3ec7c23d96be"
    BOT_TOKEN = "5677957515:AAGpvl0FdgNZ6O0Oo-y8qGNvTC4S4N2vyh0"
    MUST_JOIN = "holycardershq"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
    INSTA_USERNAME = "amanda_townes_"
    INSTA_PASSWORD = "ricchydC@1"
    # Fill the Values

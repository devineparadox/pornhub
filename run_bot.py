# run_bot.py
import sys
import os

# Add the project root to the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import and run the bot
from my_bot import bot

if __name__ == "__main__":
    bot.main()

# time_tick_quiz.py

import requests
import html
import random
import threading
import time

CATEGORY_URL = "https://opentdb.com/api_category.php"
QUESTION_URL = "https://opentdb.com/api.php"
TIME_LIMIT = 15  # seconds per question

# ------------------ api functionss ------------------

def fetch_categories():
    """
    fetches trivia categories from the API.
    """
    pass

def fetch_questions(amount=10):
    """
    fetches the questions based on given filters.
    """
    pass

# ------------------ user input selection ------------------

def select_category():
    """
    prompts user to select a category from the list.
    """
    pass

def select_difficulty():
    """
    prompst user to select question difficulty.
    """
    pass

def select_question_type():
    """
    prompts the user to select type of questions (multiple/boolean).
    """
    pass

# ------------------ quiz logicc ------------------

def ask_question():
    """
    presents a question to the user with a countdown timer.
    """
    pass

def select_quiz_options(categories):
    """
    gathers all the quiz options and fetch questions accordingly.
    """
    pass

# ------------------ main fucntion ------------------

def main():
    """
    Entry point for the TimeTickQuiz game.
    """
    pass

if __name__ == "__main__":
    main()

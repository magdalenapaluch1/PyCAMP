"""CONSOLE QUIZ"""

import json
import datetime

from QuestionSet import QuestionSet

SCORE_FILENAME = "results.json"

def save_score(name, new_score):
    """Save new score to file.
    Function checks if name is already in results.
    If name exist - check the result, result is saved only when it's better.
    Parameters:
    name(str): user name
    new_score(int): user points
    """
    with open(SCORE_FILENAME, 'r', encoding="utf8") as scores_file:
        current_scores = json.load(scores_file)

    name_already_in_list = False
    for score in current_scores:
        if name == score["name"]:
            name_already_in_list = True
            if new_score > score["score"]:
                score["score"] = new_score
                score["timestamp"] = datetime.datetime.now()

    if not name_already_in_list:
        user_score_dict = {"name": name, "score": new_score, "timestamp": datetime.datetime.now()}
        current_scores.append(user_score_dict)

    current_scores_sorted = sorted(current_scores, key=lambda d: d['score'], reverse=True)

    with open(SCORE_FILENAME, 'w', encoding="utf8") as scores_file:
        json.dump(current_scores_sorted, scores_file, default=str)


def print_top_scores(number):
    """Function print TOP given numbers of results.
    Parameters:
    number(int): number of printing scores
    """

    score_board_counter = 1
    with open(SCORE_FILENAME, 'r', encoding="utf8") as scores_file:
        scores_data = json.load(scores_file)
        print(f" {number} TOP results: ")

        for score in scores_data:
            print(f'{score_board_counter}. {score["name"]} {score["score"]}')
            score_board_counter += 1
            if score_board_counter > number:
                break

if __name__ == "__main__":
    with open('questions.json', encoding="utf8") as file:
        quiz_data = json.load(file)

    USER_SCORE = 0

    question_list = []

    for question_record in quiz_data:

        new_question = QuestionSet(question_record)
        question_list.append(new_question)
        new_question.PrintQuestion()
        new_question.PrintAnswers()
        user_answer = input("Right answer: ")
        if new_question.CheckAnswer(user_answer) is True:
            USER_SCORE += 1

    user_name = input("Your name: ")

    print(f'{user_name}, you earn {USER_SCORE} / {len(quiz_data)} points!')

    save_score(user_name, USER_SCORE)

    print_top_scores(5)

#TODO
# klasa user
# zabezpieczenie danych

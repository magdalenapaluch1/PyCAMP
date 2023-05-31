import json
import datetime

from QuestionSet import QuestionSet

SCORE_FILE = "results.json"

def SaveScore(name, score):
    with open(SCORE_FILE, 'r') as scores_file:
        current_scores = json.load(scores_file)

    user_score_dict = {"name": name, "score": score, "timestamp": datetime.datetime.now()}
    current_scores.append(user_score_dict)

    current_scores_sorted = sorted(current_scores, key=lambda d: d['score'], reverse=True)

    with open(SCORE_FILE, 'w') as scores_file:
        json.dump(current_scores_sorted, scores_file, default=str)


def PrintTopScores(number):
    #wyświetlanie top wyników
    score_board_counter = 1
    with open(SCORE_FILE, 'r') as scores_file:
        scores_data = json.load(scores_file)
        print(f"Lista {number} najlepszych wyników: ")

        for score in scores_data:
            print(f'{score_board_counter}. {score["name"]} {score["score"]}')
            score_board_counter += 1
            if score_board_counter > number:
                break

if __name__ == "__main__":
    with open('questions.json') as file:
        quiz_data = json.load(file)

    #print(data)
    user_score = 0
    #wyświetlenie pytania i odpowiedzi

    question_list = []

    for question_record in quiz_data:

        new_question = QuestionSet(question_record)
        question_list.append(new_question)
        new_question.PrintQuestion()
        new_question.PrintAnswers()
        user_answer = input("Podaj poprawną odpowiedź: ")
        if new_question.CheckAnswer(user_answer) == True:
            user_score += 1

    #poproszenie użytkownika o podanie imienia
    user_name = input("Podaj swoje imię: ")

    #wyświetlenie wyniku z podanym imieniem gracza
    print(f'{user_name}, zdobywasz {user_score} / {len(quiz_data)} pkt!')

    SaveScore(user_name, user_score)

    PrintTopScores(5)

#TODO
# sprawdzac czy uzytkownik juz jest w wynikach, jesli tak to aktualizowac wynik jesli lepszy
# klasa user
# zabezpieczenie danych

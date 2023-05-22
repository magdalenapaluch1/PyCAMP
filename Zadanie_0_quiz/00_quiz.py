import json
import datetime
from string import ascii_lowercase

with open('questions.json') as file:
    data = json.load(file)

#print(data)
user_score = 0
#wyświetlenie pytania i odpowiedzi

for question_set in data:
    print(question_set['question'])
    i = 0
    for answer in (question_set['answers']):
        print(ascii_lowercase[i] + ". " + str(answer))
        i = i + 1

    #użytkownik podaje swoją odpowiedź
    user_answer = input("Podaj poprawną odpowiedź: ")

    #porównanie odp użytkownika z prawidłową
    if user_answer == question_set['right answer']:
        print("Brawo, prawidłowa odpowiedź!")
        user_score += 1
    else:
        print("Zła odpowiedź.")

#poproszenie użytkownika o podanie imienia

user_name = input("Podaj swoje imię: ")

#wyświetlenie wyniku z podanym imieniem gracza

print(f'{user_name}, zdobywasz {user_score} / {len(data)} pkt!')

#plik z wynikami użytkowników

with open('scores.txt', 'a') as scores_file:
    # Zapisz wartość do pliku
    scores_file.write(f'{user_name}, {user_score}, {datetime.datetime.now()}' + '\n')

#wyświetlanie TOP 5 wyników
score_board_counter = 1
with open('scores.txt', 'r') as scores_file:
    lines = scores_file.readlines()
    print("Lista 5 najlepszych wyników: ")
    for line in lines:
        print(f'{score_board_counter}. {line}', end='')
        score_board_counter += 1
        if score_board_counter > 5:
            break
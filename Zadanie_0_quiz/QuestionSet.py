from string import ascii_lowercase

class QuestionSet():
    def __init__(self, question_set_dict):
        self.question = question_set_dict['question']
        self.answers = question_set_dict['answers']
        self.correct_answer = question_set_dict['right answer']

    def PrintQuestion(self):
        print(self.question)

    def PrintAnswers(self):
        i = 0
        for answer in (self.answers):
            print(ascii_lowercase[i] + ". " + str(answer))
            i = i + 1

    def CheckAnswer(self, user_answer):
        if user_answer == self.correct_answer:
            print("Brawo, prawidłowa odpowiedź!")
            return True
        else:
            print("Zła odpowiedź.")
            return False
class Quizbrain:

    def __init__(self, list):
        self.question_number = 0
        self.question_list = list

    def still_has_questions(self):
        return self.question_number<len(self.question_list)

    def Qizbrain(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f'Q.{self.question_number}: {current_question.text}')

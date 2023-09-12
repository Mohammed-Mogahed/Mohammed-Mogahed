from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

score = 0
question_bank=[]

for i in question_data:
    question_text=i['text']
    question_answer = i['answer']
    question_bank.append(Question(question_text,question_answer))

quiz = Quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.Qizbrain()



from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random


def start_quiz():
    question_bank = []
    i = 0
    for _ in question_data:
        question = question_data[i]["question"]
        answer = question_data[i]["correct_answer"]
        new_question = Question(question, answer)
        question_bank.append(new_question)
        i += 1
    random.shuffle(question_bank)
    my_quiz = QuizBrain(question_bank)
    my_quiz.ask_question()


start_quiz()

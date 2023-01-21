class QuizBrain:
    def __init__(self, question_bank):
        self.question_list = question_bank
        self.question_number = 0
        self.question_correct = 0
        self.question_answer = ""

    def ask_question(self):
        print(f"Question {self.question_number+1}: {self.question_list[self.question_number].text}")
        self.question_answer = input("True or False?: ").lower()
        if self.question_answer == self.question_list[self.question_number].answer:
            print("That is correct!")
            self.question_correct += 1
            self.question_number += 1
        elif self.question_answer != self.question_list[self.question_number].answer:
            print("Incorrect...")
            self.question_number += 1
        print(f"{self.question_correct}/{self.question_number} Correct")
        while self.question_number < len(self.question_list):
            self.ask_question()
        print(f"Quiz finished! You answered {self.question_correct} questions correctly")

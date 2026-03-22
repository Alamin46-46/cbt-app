from datetime import datetime

class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.start_time = datetime.now()

    def add_question(self, question):
        self.questions.append(question)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1

    def get_score(self):
        return self.score
from flask import Flask, render_template, request, redirect
from models import Question, Quiz
from datetime import datetime

app = Flask(__name__)
quiz = Quiz()

# Sample questions
quiz.add_question(Question("What is 2 + 2?", ["2", "3", "4", "5"], "4"))
quiz.add_question(Question("what state is the Capital of Nigeria?", ["Lagos", "Abuja", "Kano", "Ibadan"], "Abuja"))
quiz.add_question(Question("who is the current governor of Kano?", ["Kwankwaso", "Ganduje", "Abba K Yusuf", "Gawuna"], "Abba K Yusuf"))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz_page():
    if request.method == 'POST':
        answers = request.form
        for i, q in enumerate(quiz.questions):
            user_answer = answers.get(f"q{i}")
            quiz.check_answer(user_answer, q.answer)

        return redirect('/result')

    return render_template('quiz.html', questions=quiz.questions)


@app.route('/result')
def result():
    score = quiz.get_score()
    time = datetime.now().strftime("%H:%M:%S")
    return render_template('result.html', score=score, total=len(quiz.questions), time=time)


if __name__ == '__main__':
    app.run(debug=True)
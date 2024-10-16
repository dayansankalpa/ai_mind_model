from flask import Blueprint, render_template, request
from .model import get_questions, calculate_personality_type

main = Blueprint('main', __name__)

@main.route('/')
def index():
    questions = get_questions()
    return render_template('index.html', questions=questions)

@main.route('/submit', methods=['POST'])
def submit():
    user_answers = request.form.to_dict(flat=False)
    scores = {key: int(value[0]) for key, value in user_answers.items()}
    personality_type = calculate_personality_type(scores)
    return render_template('result.html', personality_type=personality_type)

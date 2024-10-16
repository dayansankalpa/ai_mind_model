import json

def load_json(filename):
    with open(filename) as f:
        return json.load(f)

def get_questions():
    questions_data = load_json('data/questions.json')
    return questions_data

def calculate_personality_type(scores):
    # Simple scoring logic: threshold example for personality types
    # This can be modified to use the actual scoring based on your criteria
    total_score = sum(scores.values())
    
    if total_score >= 30:  # Adjust these values based on your scoring criteria
        return "The Compassionate"
    elif total_score >= 25:
        return "The Mindful"
    elif total_score >= 20:
        return "The Generous"
    elif total_score >= 15:
        return "The Patient"
    elif total_score >= 10:
        return "The Wise"
    elif total_score >= 5:
        return "The Self-controlled"
    else:
        return "The Resilient"

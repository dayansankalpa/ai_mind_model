import json

def load_json(filename):
    with open(filename) as f:
        return json.load(f)

def get_questions():
    questions_data = load_json('data/questions.json')
    return questions_data

def calculate_personality_type(scores):
    # Calculate the total score from the scores dictionary
    total_score = sum(scores.values())

    # Define personality types and their corresponding score thresholds
    if total_score >= 60:  # Adjust these values based on your scoring criteria
        return "The Visionary"
    elif total_score >= 50:
        return "The Architect"
    elif total_score >= 40:
        return "The Nurturer"
    elif total_score >= 35:
        return "The Activist"
    elif total_score >= 30:
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

# Example usage
if __name__ == "__main__":
    scores = {
        "question_1": 5,
        "question_2": 3,
        "question_3": 4,
        "question_4": 5,
        "question_5": 2,
        "question_6": 4,
        "question_7": 5,
        "question_8": 3,
        "question_9": 4,
        "question_10": 2,
        "question_11": 3,
        "question_12": 4,
    }
    
    personality_type = calculate_personality_type(scores)
    print(f"Your personality type is: {personality_type}")

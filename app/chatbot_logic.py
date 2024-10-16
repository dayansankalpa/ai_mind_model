import json

def load_data():
    with open('data/mental_factors.json') as f:
        mental_factors = json.load(f)
    with open('data/personality_types.json') as f:
        personality_types = json.load(f)
    with open('data/questions.json') as f:
        questions = json.load(f)
    return mental_factors, personality_types, questions

def process_response(user_responses):
    mental_scores = {mf['id']: 0 for mf in load_data()[0]}
    
    for response in user_responses:
        # Increment score based on the user's response
        mental_scores[response['mental_factor_id']] += response['score']
    
    return mental_scores

def calculate_personality_type(mental_scores):
    # Simple logic to calculate personality type based on scores
    highest_score = max(mental_scores.values())
    personality_type = None
    
    for mf_id, score in mental_scores.items():
        if score == highest_score:
            personality_type = mf_id  # Return the ID of the mental factor with the highest score

    return personality_type

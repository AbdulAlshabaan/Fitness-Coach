from flask import Flask, request, jsonify

app = Flask(__name__)

# --- Home Route ---
@app.route('/')
def home():
    return "Welcome to the Fitness App!"

# --- User Registration Endpoint ---
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    age = data.get('age')
    weight = data.get('weight')
    gender = data.get('gender')

    if not all([email, password, age, weight, gender]):
        return jsonify({'error': 'Missing required fields'}), 400

    # Mock user registration (No Firebase here)
    user_id = email.replace("@", "_").replace(".", "_")  # Generate mock user_id
    user_data = {
        'email': email,
        'age': age,
        'weight': weight,
        'gender': gender,
        'workout_preferences': {}
    }

    # Simulate saving the user to a database
    print(f"User registered: {user_data}")

    return jsonify({'message': 'User registered successfully', 'user_id': user_id}), 200

# --- AI Chatbot Endpoint ---
@app.route('/chat', methods=['POST'])
def ai_chat():
    data = request.json
    question = data.get('question')

    if not question:
        return jsonify({'error': 'No question provided'}), 400

    # Mock AI response (Static responses for now)
    if 'biceps' in question.lower():
        response = "You can do bicep curls or pull-ups to strengthen your biceps."
    elif 'abs' in question.lower():
        response = "Planks and sit-ups are great for your abs."
    else:
        response = "I'm not sure. Try general fitness exercises like push-ups."

    return jsonify({'response': response}), 200

# --- Workout Plan Endpoint ---
@app.route('/workout', methods=['POST'])
def generate_workout():
    data = request.json
    age = data.get('age')
    weight = data.get('weight')
    gender = data.get('gender')
    goal = data.get('goal')  # e.g., muscle_gain, weight_loss

    if not all([age, weight, gender, goal]):
        return jsonify({'error': 'Missing required fields'}), 400

    # Example workout plan logic
    if goal == 'muscle_gain':
        workout_plan = {
            'day_1': ['Push-Ups', 'Bicep Curls', 'Squats'],
            'day_2': ['Bench Press', 'Deadlifts', 'Plank'],
            'day_3': ['Rest']
        }
    elif goal == 'weight_loss':
        workout_plan = {
            'day_1': ['Jogging', 'Burpees', 'Jumping Jacks'],
            'day_2': ['Cycling', 'Plank', 'Mountain Climbers'],
            'day_3': ['Rest']
        }
    else:
        workout_plan = {'error': 'Unknown goal'}

    return jsonify({'workout_plan': workout_plan}), 200

# --- Reminder Endpoint ---
@app.route('/reminder', methods=['POST'])
def set_reminder():
    data = request.json
    user_id = data.get('user_id')
    reminder_time = data.get('reminder_time')

    if not all([user_id, reminder_time]):
        return jsonify({'error': 'Missing required fields'}), 400

    # Simulate saving the reminder to a database
    reminder_data = {
        'user_id': user_id,
        'reminder_time': reminder_time
    }
    print(f"Reminder set: {reminder_data}")

    return jsonify({'message': 'Reminder set successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)

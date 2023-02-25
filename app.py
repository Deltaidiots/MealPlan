from flask import Flask, render_template
import random

app = Flask(__name__)

# Define meal options
breakfast_options = ['Omelette with vegetables', 'Greek yogurt with berries and nuts', 'Avocado toast with scrambled eggs', 'Protein smoothie with spinach and banana']
lunch_options = ['Grilled chicken salad with mixed greens and vegetables', 'Vegetable stir-fry with tofu and brown rice', 'Tuna salad with avocado and whole grain crackers', 'Chicken or beef fajita bowl with vegetables and quinoa']
dinner_options = ['Baked salmon with roasted vegetables', 'Grilled steak with sweet potato and asparagus', 'Vegan chili with brown rice and avocado', 'Turkey or beef meatballs with zucchini noodles and tomato sauce']

# Define meal plan for each day of the week
meal_plan = {
    'Monday': {
        'Breakfast': breakfast_options[0],
        'Lunch': lunch_options[0],
        'Dinner': dinner_options[0]
    },
    'Tuesday': {
        'Breakfast': breakfast_options[1],
        'Lunch': lunch_options[1],
        'Dinner': dinner_options[1]
    },
    'Wednesday': {
        'Breakfast': breakfast_options[2],
        'Lunch': lunch_options[2],
        'Dinner': dinner_options[2]
    },
    'Thursday': {
        'Breakfast': breakfast_options[3],
        'Lunch': lunch_options[3],
        'Dinner': dinner_options[3]
    },
    'Friday': {
        'Breakfast': breakfast_options[0],
        'Lunch': lunch_options[0],
        'Dinner': dinner_options[0]
    },
    'Saturday': {
        'Breakfast': breakfast_options[1],
        'Lunch': lunch_options[1],
        'Dinner': dinner_options[1]
    },
    'Sunday': {
        'Breakfast': breakfast_options[2],
        'Lunch': lunch_options[2],
        'Dinner': dinner_options[2]
    }
}

# Function to get meal suggestion
def get_meal_suggestion(meal_type):
    meal_options = None
    if meal_type == 'Breakfast':
        meal_options = breakfast_options
    elif meal_type == 'Lunch':
        meal_options = lunch_options
    elif meal_type == 'Dinner':
        meal_options = dinner_options
    else:
        return None
    
    suggestion = random.choice(meal_options)
    return suggestion

# Route for the meal plan page
@app.route('/')
def meal_plan_page():
    return render_template('meal_plan.html', meal_plan=meal_plan)

# Route for the alternative meal suggestions page
@app.route('/suggestions')
def meal_suggestions_page():
    suggestions = {}
    for meal_type in ['Breakfast', 'Lunch', 'Dinner']:
        suggestions[meal_type] = get_meal_suggestion(meal_type)
    return render_template('meal_suggestions.html', suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True)

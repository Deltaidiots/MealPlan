import random

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

# Get meal plan for the week
print("Here's your meal plan for the week:")
for day, meals in meal_plan.items():
    print(f"\n{day}")
    for meal_type, meal in meals.items():
        print(f"{meal_type}: {meal}")

# Get alternative meal suggestions
print("\nIf you don't like a meal, here are some alternative options:")
for meal_type in ['Breakfast', 'Lunch', 'Dinner']:
    suggestion = get_meal_suggestion(meal_type)
    print(f"{meal_type}: {suggestion}")

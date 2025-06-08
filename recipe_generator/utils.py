import json
from pathlib import Path

def save_to_json(data, filename):
    """Save data to JSON file"""
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def load_from_json(filename):
    """Load data from JSON file"""
    with open(filename) as f:
        return json.load(f)

def format_recipe_output(recipe_text, include_shopping_list=False, generator=None):
    """Format recipe output with optional shopping list"""
    output = f"RECIPE:\n{recipe_text}\n"
    
    if include_shopping_list and generator:
        shopping_list = generator.generate_shopping_list(recipe_text)
        output += f"\nSHOPPING LIST:\n{shopping_list}\n"
    
    return output

def validate_ingredients(ingredients):
    """Basic validation for ingredients list"""
    if not isinstance(ingredients, list):
        raise ValueError("Ingredients must be a list")
    if len(ingredients) < 1:
        raise ValueError("At least one ingredient is required")
    return True
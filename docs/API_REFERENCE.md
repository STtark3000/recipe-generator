# Recipe Generator API Reference

## RecipeGenerator Class

### Methods

#### `generate_recipe(ingredients, **options)`
Generates a recipe based on provided ingredients and options.

**Parameters:**
- `ingredients` (list): List of main ingredients
- `options` (dict): Optional parameters:
  - `diet`: Dietary preference (vegan, vegetarian, keto, etc.)
  - `cuisine`: Cuisine style (Italian, Mexican, etc.)
  - `difficulty`: easy/medium/hard
  - `portions`: Number of servings
  - `allergies`: Allergy restrictions
  - `meal_type`: breakfast/lunch/dinner/snack
  - `cooking_time`: Max cooking time in minutes

**Returns:** Formatted recipe text

#### `generate_shopping_list(recipe_text)`
Generates a shopping list for a given recipe.

**Parameters:**
- `recipe_text`: The full text of a generated recipe

**Returns:** Formatted shopping list
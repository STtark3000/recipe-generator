# Recipe Generator User Guide

## Installation
1. Install Python 3.8+
2. Clone this repository
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Create a `.env` file with your API keys

## Basic Usage
```python
from recipe_generator import RecipeGenerator

# Initialize
generator = RecipeGenerator()

# Generate recipe
recipe = generator.generate_recipe(
    ["chicken", "potatoes"],
    cuisine="Mediterranean",
    portions=4
)

# Generate shopping list
shopping_list = generator.generate_shopping_list(recipe)
```

## Sample Recipes
Pre-generated samples are available in `samples/sample_recipes.json`
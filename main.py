from recipe_generator import RecipeGenerator
from recipe_generator.utils import save_to_json, format_recipe_output

def main():
    # Initialize the generator
    generator = RecipeGenerator()
    
    # Example with Spoonacular nutrition API
    ingredients = ["salmon fillet", "quinoa", "spinach"]
    options = {
        'diet': 'gluten-free',
        'cuisine': 'Mediterranean',
        'portions': 2
    }
    
    # Use the correct method name
    recipe = generator.create_recipe_with_nutrition(ingredients, **options)
    
    print(format_recipe_output(recipe, include_shopping_list=True, generator=generator))
    
    # Generate and save samples
    generate_samples(generator)

def generate_samples(generator):
    sample_cases = [
        (["chickpeas", "tomatoes", "cucumber"], {'diet': 'vegetarian', 'cuisine': 'Middle Eastern'}),
        (["beef", "potatoes", "carrots"], {'difficulty': 'easy', 'meal_type': 'dinner'}),
        # Add more cases as needed
    ]
    
    samples = []
    for idx, (ingredients, options) in enumerate(sample_cases[:20], 1):
        try:
            recipe = generator.create_recipe_with_nutrition(ingredients, **options)
            samples.append({
                'id': idx,
                'ingredients': ingredients,
                'options': options,
                'recipe': recipe
            })
            print(f"Generated sample {idx}")
        except Exception as e:
            print(f"Error generating sample {idx}: {e}")
    
    save_to_json(samples, 'samples/sample_recipes.json')
    print("Saved samples to samples/sample_recipes.json")

if __name__ == "__main__":
    main()
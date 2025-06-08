import google.generativeai as genai
from dotenv import load_dotenv
import os
import re
from .nutrition_api import NutritionAPI

load_dotenv()

class RecipeGenerator:
    def __init__(self):
        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        self.nutrition_api = NutritionAPI()
    
    def create_recipe(self, ingredients, **options):
        """Main recipe generation method (renamed from generate_recipe)"""
        defaults = {
            'diet': None,
            'cuisine': None,
            'difficulty': 'medium',
            'portions': 2,
            'allergies': None,
            'meal_type': None,
            'cooking_time': None
        }
        options = {**defaults, **options}
        
        prompt = self._build_prompt(ingredients, options)
        recipe = self._get_recipe_from_ai(prompt)
        enhanced_recipe = self._enhance_recipe(recipe, options)
        
        return enhanced_recipe
    
    def create_recipe_with_nutrition(self, ingredients, **options):
        """Generate recipe with detailed nutrition analysis"""
        recipe = self.create_recipe(ingredients, **options)
        
        # Enhanced nutrition analysis
        detailed_nutrition = self.nutrition_api.estimate_nutrition(recipe)
        
        if detailed_nutrition:
            # Remove basic nutrition if exists
            recipe = re.sub(r'Nutritional Information:[\s\S]*?(?=\n\n)', '', recipe)
            recipe += f"\n\nDetailed Nutritional Analysis:\n{detailed_nutrition}"
        
        return recipe
    
    def _build_prompt(self, ingredients, options):
        prompt_parts = [
            "Create a detailed recipe using these ingredients:",
            ", ".join(ingredients) + ".",
            f"Cuisine: {options['cuisine']}." if options['cuisine'] else "",
            f"Diet: {options['diet']}." if options['diet'] else "",
            f"Allergies: {options['allergies']}." if options['allergies'] else "",
            f"Meal type: {options['meal_type']}." if options['meal_type'] else "",
            f"Difficulty: {options['difficulty']}.",
            f"Serves: {options['portions']}.",
            f"Max cooking time: {options['cooking_time']} mins." if options['cooking_time'] else "",
            "Include: ingredients with quantities, step-by-step instructions,",
            "prep/cook times, serving suggestions, and possible substitutions.",
            "Format with clear sections: Name, Description, Ingredients,",
            "Instructions, Times, Servings, Nutrition, Notes."
        ]
        return " ".join([p for p in prompt_parts if p])
    
    def _get_recipe_from_ai(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text
    
    def _enhance_recipe(self, recipe, options):
        # Basic nutrition placeholder
        recipe += "\n\nNutritional Information: Basic estimates included"
        
        # Add portion scaling notes
        if options['portions'] != 2:
            recipe += f"\n\nNote: Recipe scaled for {options['portions']} servings."
        
        return recipe
    
    def generate_shopping_list(self, recipe_text):
        prompt = f"""
        Create a categorized shopping list for this recipe:
        
        {recipe_text}
        
        Organize by: Produce, Dairy, Meat, Dry Goods, Spices, etc.
        Include exact quantities needed.
        """
        return self._get_recipe_from_ai(prompt)
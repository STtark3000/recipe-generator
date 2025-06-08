import requests
from dotenv import load_dotenv
import os
import re

load_dotenv()

class NutritionAPI:
    def __init__(self):
        self.api_key = os.getenv('SPOONACULAR_API_KEY')
        self.base_url = "https://api.spoonacular.com"
    
    def estimate_nutrition(self, recipe_text):
        try:
            # Extract ingredients from recipe text
            ingredients = self._extract_ingredients(recipe_text)
            
            # Get nutrition for each ingredient
            nutrition_data = []
            for ing in ingredients[:5]:  # Limit to 5 ingredients for free tier
                nutr = self._get_ingredient_nutrition(ing)
                if nutr:
                    nutrition_data.append(nutr)
            
            return self._aggregate_nutrition(nutrition_data)
        except Exception as e:
            print(f"Nutrition API error: {e}")
            return None
    
    def _extract_ingredients(self, recipe_text):
        """Extract ingredients list from recipe text"""
        # Look for ingredients section
        ingredients_match = re.search(r'Ingredients:([\s\S]*?)Instructions:', recipe_text, re.IGNORECASE)
        if not ingredients_match:
            return []
        
        ingredients_section = ingredients_match.group(1)
        # Split into individual ingredients
        ingredients = [
            line.strip('-* ').strip() 
            for line in ingredients_section.split('\n') 
            if line.strip()
        ]
        return ingredients
    
    def _get_ingredient_nutrition(self, ingredient):
        """Get nutrition for a single ingredient"""
        url = f"{self.base_url}/food/ingredients/search"
        params = {
            'apiKey': self.api_key,
            'query': ingredient,
            'number': 1
        }
        
        try:
            # Search for ingredient ID first
            search_res = requests.get(url, params=params)
            search_res.raise_for_status()
            data = search_res.json()
            
            if not data.get('results'):
                return None
                
            ingredient_id = data['results'][0]['id']
            
            # Get nutrition info
            nutr_url = f"{self.base_url}/food/ingredients/{ingredient_id}/information"
            nutr_params = {
                'apiKey': self.api_key,
                'amount': 100,  # 100g standard amount
                'unit': 'grams'
            }
            
            nutr_res = requests.get(nutr_url, params=nutr_params)
            nutr_res.raise_for_status()
            return nutr_res.json()
            
        except Exception as e:
            print(f"Error getting nutrition for {ingredient}: {e}")
            return None
    
    def _aggregate_nutrition(self, nutrition_data):
        """Combine nutrition data from multiple ingredients"""
        if not nutrition_data:
            return "Nutrition data not available"
        
        total = {
            'calories': 0,
            'protein': 0,
            'carbs': 0,
            'fat': 0
        }
        
        for item in nutrition_data:
            if 'nutrition' in item:
                nutr = item['nutrition']
                total['calories'] += nutr['calories']['value']
                total['protein'] += nutr['protein']['value']
                total['carbs'] += nutr['carbs']['value']
                total['fat'] += nutr['fat']['value']
        
        return f"""Nutrition per serving (estimated):
Calories: {total['calories']:.0f} kcal
Protein: {total['protein']:.1f}g
Carbohydrates: {total['carbs']:.1f}g
Fat: {total['fat']:.1f}g"""
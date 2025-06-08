# 🍳 AI Recipe Generator

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/yourusername/recipe-generator)
![License](https://img.shields.io/badge/License-MIT-green.svg)

An intelligent recipe generation system using Google AI Studio and Spoonacular API that creates personalized recipes based on ingredients and dietary preferences.

## ✨ Features

- 🥗 Generate recipes from any list of ingredients
- 🌱 Support for dietary restrictions (vegan, gluten-free, etc.)
- 🍲 Multiple cuisine styles (Italian, Asian, Mexican, etc.)
- 📊 Automatic nutritional information
- 🛒 Shopping list generation
- ⏱️ Cooking time and difficulty levels

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google AI Studio API key
- Spoonacular API key (optional for nutrition data)

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/recipe-generator.git
cd recipe-generator

2.Install dependencies:
```bash
pip install -r requirements.txt

3.Create a .env file:
```bash
echo "GOOGLE_API_KEY=your_key_here" > .env
echo "SPOONACULAR_API_KEY=your_key_here" >> .env

Usage
Run the recipe generator:
```bash
python main.py


Example output:
🍴 Generated Recipe: Garlic Butter Salmon with Quinoa

📝 Ingredients:
- 2 salmon fillets
- 1 cup quinoa
- 2 tbsp butter
- 3 cloves garlic
- 1 lemon
...

🔪 Instructions:
1. Cook quinoa according to package instructions
2. Melt butter in pan, add minced garlic
3. Sear salmon skin-side down for 4 minutes
...

⏱️ Cooking Time: 25 minutes
📊 Nutrition (per serving): 450 kcal, 35g protein

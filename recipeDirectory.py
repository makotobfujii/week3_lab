import bisect
import random
import requests

# Recipe class to represent each individual recipe
class Recipe:
    def __init__(self, name, dish_type, ingredients, prep_time, area, category, instructions, servings):
        self.name = name
        self.type = dish_type
        self.ingredients = sorted(ingredients)  # Ensure ingredients are sorted for binary search
        self.prep_time = prep_time
        self.area = area
        self.category = category
        self.instructions = instructions
        self.servings = servings

    def __str__(self):
        return (f"{self.name} ({self.type}) - Prep time: {self.prep_time} min\n"
                f"Category: {self.category} | Area: {self.area} | Serves: {self.servings}\n"
                f"Ingredients: {', '.join(self.ingredients)}\nInstructions: {self.instructions}")


# RecipeDirectory class to manage recipes and perform searches
class RecipeDirectory:
    def __init__(self):
        self.recipes = []
        self.recipes_by_name = []
        self.recipes_by_prep_time = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        self.recipes_by_name = sorted(self.recipes, key=lambda r: r.name.lower())
        self.recipes_by_prep_time = sorted(self.recipes, key=lambda r: r.prep_time)

    def binary_search_by_name(self, name):
        # Binary search based on recipe name
        names = [r.name.lower() for r in self.recipes_by_name]
        index = bisect.bisect_left(names, name.lower())
        if index != len(names) and names[index] == name.lower():
            return self.recipes_by_name[index]
        return None

    def binary_search_by_prep_time(self, max_time):
        # Binary search based on maximum preparation time
        times = [r.prep_time for r in self.recipes_by_prep_time]
        index = bisect.bisect_right(times, max_time)
        return self.recipes_by_prep_time[:index]

    def binary_search_in_ingredients(self, sorted_ingredients, ingredient):
        # Binary search on the ingredients of a recipe
        index = bisect.bisect_left(sorted_ingredients, ingredient)
        return index != len(sorted_ingredients) and sorted_ingredients[index] == ingredient

    def search_by_ingredients(self, ingredients):
        # Use binary search for each ingredient in the recipe's sorted ingredient list
        results = []
        for recipe in self.recipes:
            if all(self.binary_search_in_ingredients(recipe.ingredients, ingredient) for ingredient in ingredients):
                results.append(recipe)
        return results

    def get_random_meal(self):
        # Retrieve a random meal from TheMealDB API
        response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
        data = response.json()['meals'][0]
        ingredients = [data[f'strIngredient{i}'] for i in range(1, 21) if data[f'strIngredient{i}']]
        return Recipe(
            name=data['strMeal'],
            dish_type=data['strCategory'],
            ingredients=ingredients,
            prep_time=30,  # Mocked, as TheMealDB doesn't provide prep time
            area=data['strArea'],
            category=data['strCategory'],
            instructions=data['strInstructions'],
            servings=4
        )


# RecipeSearchUI class to handle user interface and interactions
class RecipeSearchUI:
    def __init__(self, directory):
        self.directory = directory

    def display_menu(self):
        print("\nWelcome to the Cooking Recipe Directory!")
        print("1. Search by recipe name")
        print("2. Search by maximum preparation time")
        print("3. Search by ingredients")
        print("4. Get a random meal of the day")
        print("5. Exit")
        choice = input("\nEnter your choice: ")
        return choice

    def handle_search(self):
        while True:
            choice = self.display_menu()

            if choice == "1":
                name = input("Enter the recipe name: ").strip()
                result = self.directory.binary_search_by_name(name)
                if result:
                    print(f"\nRecipe found:\n{result}")
                else:
                    print("\nRecipe not found.")

            elif choice == "2":
                max_time = int(input("Enter the maximum preparation time (in minutes): ").strip())
                results = self.directory.binary_search_by_prep_time(max_time)
                if results:
                    print("\nRecipes found:")
                    for recipe in results:
                        print(recipe)
                else:
                    print("\nNo recipes found under that preparation time.")

            elif choice == "3":
                ingredients = input("Enter ingredients (comma-separated): ").strip().lower().split(", ")
                results = self.directory.search_by_ingredients(ingredients)
                if results:
                    print("\nRecipes found:")
                    for recipe in results:
                        print(recipe)
                else:
                    print("\nNo recipes found with those ingredients.")

            elif choice == "4":
                random_meal = self.directory.get_random_meal()
                print("\nRandom meal of the day:")
                print(random_meal)

            elif choice == "5":
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Try again.")


# Sample usage
if __name__ == "__main__":
    # Create the recipe directory
    recipe_directory = RecipeDirectory()

    # Add some sample recipes
    recipe_directory.add_recipe(Recipe("Spaghetti Bolognese", "Main Course", ["spaghetti", "ground beef", "tomato sauce"], 45, "Italian", "Main Course", "Cook pasta and add sauce", 4))
    recipe_directory.add_recipe(Recipe("Pancakes", "Breakfast", ["flour", "milk", "eggs"], 20, "American", "Breakfast", "Mix ingredients and cook", 2))
    recipe_directory.add_recipe(Recipe("Caesar Salad", "Salad", ["lettuce", "croutons", "parmesan"], 15, "American", "Salad", "Toss ingredients", 2))
    recipe_directory.add_recipe(Recipe("Chocolate Cake", "Dessert", ["flour", "sugar", "chocolate"], 60, "French", "Dessert", "Mix and bake", 8))

    # Create and run the user interface
    ui = RecipeSearchUI(recipe_directory)
    ui.handle_search()

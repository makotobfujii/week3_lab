# Recipe Directory Project Plan

## Inputs:
1. Initial response to the random meal of the day
  - User can choose to select recipe by inputting:
    - Yes
    - No
2. Filter/Search keywords:
  - Options:     
    - Category | www.themealdb.com/api/json/v1/1/filter.php?c=<ENTER_CATEGORY>
    - Area (country) | www.themealdb.com/api/json/v1/1/filter.php?a=<ENTER_COUNTRY>
    - Main Ingredient | www.themealdb.com/api/json/v1/1/filter.php?i=<ENTER_INGREDIENT>
    
## Outputs: 
1. Drop down menu for each filter/search keyword. Each drop down will have a list of all possible options for the category
  - Return list of all possible categories, areas, and ingredients using: www.themealdb.com/api/json/v1/1/list.php?c=list
2. Randomly selected "meal of the day". Displayed when user first starts program
  - Random dish will be selected using: www.themealdb.com/api/json/v1/1/random.php
3. Dish information, outputted after user selects a dish
  - Category
  - Area (country)
  - Ingredients
  - Cooking Instructions
  - How many dish can serve

## Data Source:
https://www.themealdb.com/api.php

## Systems: 
1. UI: Handles user input and output
2. Search System: Performs search based on user's input
3. Recipe Data: Recipe data is from [TheMealDB](https://www.themealdb.com)
4. Binary Search & Linear Search Algorithms: Provides efficient ways to search the recipes by name or preparation time.

## Interactions: 
1. UI to Recipe Data Base: The UI queries the recipe database to display list of possible filtration category options
2. UI to Search System: The UI collects user input and passes the search request to the Search System.
3. Search System to Recipe Database via API Call: Search System queries the recipe database based on user's input
4. Recipe Storage to Search System: The Recipe Storage returns relevant data, which is filtered and sorted as necessary.
5. Search System to UI: The Search System sends the results back to the UI for display.

## Class Design:
```
Recipe Class:
Purpose: To represent each individual recipe.
Attributes:
name: Name of the recipe.
type: Type of the dish (e.g., "Dessert", "Main Course").
ingredients: List of ingredients.
prep_time: Time (in minutes) to prepare the dish.
Methods:
__str__(): To provide a formatted string representation of a recipe.
```
```
RecipeDirectory Class:
Purpose: To manage the collection of recipes and perform searches.
Attributes:
recipes: A list of all stored recipes.
recipes_by_name: A list of recipes sorted by name for binary search.
recipes_by_prep_time: A list of recipes sorted by preparation time for binary search.
Methods:
add_recipe(): To add a new recipe to the directory.
binary_search_by_name(): To perform binary search by recipe name.
binary_search_by_prep_time(): To perform binary search by preparation time.
search_by_ingredients(): To perform a linear search by 
```
```
RecipeSearchUI Class:
Purpose: To provide a text-based user interface for interacting with the RecipeDirectory.
Attributes:
directory: A RecipeDirectory instance.
Methods:
display_menu(): To display the user menu.
handle_search(): To process user input and delegate search requests to the RecipeDirectory.
```

# Our Ideas:
1. Application Tracker:
	- Job seekers can track their applications by specific fields. Binary search could be utilized to retrieve specific applications by date, location, company etc.
2. Inventory Management Tool:
	- Can be used to track stock levels of products. Users search for a product id and binary search can be used to find the product if the list is sorted
3. Cooking Recipe Directory:
	- Users can search for a specific dish they are interested in cooking. Binary search can be utilized to search for specific recipes based on dish type, ingrediant, time to prepare dish etc.

# AI Generated Ideas: 
1. **Prompt:** Consider the role of an manager at a coffee shop. His job requires for him to restock ingredients, overlook repairs, and other general day to day tasks. He can do most of the tasks easily but can get overwhelmed during store rushes. What are some python coding project ideas that use binary search functions that can assist him?
	- **Idea:** Repair Schedule Optimizer
		- Idea: The manager needs to keep track of scheduled repairs for equipment (e.g., espresso machines, grinders). Use a binary search to quickly find and update repair dates when needed, ensuring the shop never misses a maintenance check.
		- How it works:
		- Keep a sorted list of equipment repairs and scheduled dates.
		- Binary search can help locate specific equipment quickly to see when the next maintenance is scheduled.
		- Easily update or reschedule repairs by finding the entry via binary search.
		- Extension: Implement a notification system that reminds the manager of upcoming repairs.

2. **Prompt:** You are a chemist and you have some python skills. You are trying to come up with a few projects that would be useful for you and your lab team. By using binary search in Python, what project ideas can you come up with?
	- **Idea:** Chemical Compound Database
		- Description: Develop a searchable database for chemical compounds where you can quickly retrieve information based on different attributes like molecular weight, boiling point, or pH.
		- Key Features:
			- Store chemical compounds with attributes like molecular weight, boiling point, melting point, etc.
	    		- Implement binary search to quickly find compounds based on these attributes.
	    		- Provide functionalities to sort compounds based on different criteria (e.g., molecular weight, boiling point).

3. **Prompt:** You are a new social media marketing team member for a company that specializes in automated cat litter boxes. You are trying to come up with a solution to drive community engagement for your companies social media channels. Utilizing binary search in the python programming language, are there any project ideas that can assist you with improving engagement? Please respond only with project ideas and not with code.
	- **Idea:** Image vs. Video Content Comparison
		- Objective: Utilize binary search to compare engagement rates between different types of content (images, videos, polls) to find which medium performs best.
Benefit: Helps in tailoring content strategy by focusing on the content format that drives the most interaction.		

## Reflection: 
The most promising idea for our group was the Cooking Recipe Directory (See **Idea Selection** for explanation). Other promising ideas were the Inventory Management Tool and the Chemical Compound Database. The Inventory Management Tool could be highly useful for small businesses, where binary search could help quickly retrieve stock information from a sorted list. Similarly, the Chemical Compound Database would benefit scientists and researchers, allowing them to find specific chemical attributes efficiently. Both ideas focus on data organization and quick retrieval, making them highly applicable in professional settings.

# Idea Selection:
We selected the **Cooking Recipe Directory** project because we find it both practical and educational. We often look up recipes, so creating a program where users can search for specific dishes based on criteria like dish type, ingredients, or preparation time feels like something we could use in everyday life. This project also allows us to apply binary search, which is a great way to make searching more efficient. By organizing the recipes in a sorted list (e.g., based on cooking time or alphabetical order), we can use binary search to quickly find a recipe, cutting down the search time significantly compared to a linear search. It’s a useful way to reinforce our understanding of search algorithms while working on something relatable.
 
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
4. Binary Search Algorithms: Provides efficient ways to search the recipes by name or preparation time.

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

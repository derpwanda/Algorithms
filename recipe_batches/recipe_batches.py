#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients): 
	# create two lists: ingredients and recipe
	ingredients = [value for value in ingredients.values()] #list comprehension
	recipe = [value for value in recipe.values()]

	print(ingredients)
	print(recipe)
	# divide ingredients/recipe
	
	if len(ingredients) != len(recipe):
		return 0

	results = [ingredients[i]//recipe[i] for i in range(len(recipe))]
	print(results)
	# store the results in results list
	# if the min number in results less than one, return 0
	# else return the min number
	return min(results)



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
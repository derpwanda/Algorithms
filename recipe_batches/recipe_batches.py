#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients): 
	# create two lists: ingredients and recipe

	# list comprehension
	# create list / list = []
	# in that list, iterate through list, adding the dictionary values to the list
	# .values() is a python method that returns a list of values in a dictionary
	ingredients = [value for value in ingredients.values()] #list comprehension
	# same for recipe
	recipe = [value for value in recipe.values()]

	print(f"ingredients:", ingredients)
	print(f"recipe:", recipe)
	# divide ingredients/recipe
	
	# if the length of ingredients IS NOT the same as recipe list immeadiately return 0, meaning automatically, because there are missing elements in either list, that ZERO recipes can be made.
	if len(ingredients) != len(recipe):
		return 0

	# otherwise:
	# the same index of ingredient and recipe lists, for the length of recipe,  # divide(floor) the two, 
	# add/store the number in the results list
	results = [ingredients[i]//recipe[i] for i in range(len(recipe))]
	print(results)

	# return the min number
	# min() is a python method to return the smallest element in a iterable
	# https://www.programiz.com/python-programming/methods/built-in/min
	return min(results)



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
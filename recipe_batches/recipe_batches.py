#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  cookings_count = []
  print(recipe.keys())
  for key in recipe.keys():
    # print(key)
    if key not in ingredients:
      return 0
    current_max_cookings = ingredients[key] // recipe[key]
    # print(f'recipe key: {key}: {recipe[key]}, ingredients: {ingredients[key]}')
    # print(current_max_cookings)
    cookings_count.append(current_max_cookings)
    # print(cookings_count)
  # print(cookings_count)      
  max_possible_cookings = min(cookings_count)
  return max_possible_cookings
      
# print('division '+ str(198//100))
# print('batches '+str(recipe_batches({ 'milk': 100, 'butter': 50, 'cheese': 10 }, { 'milk': 198, 'butter': 52, 'cheese': 10 })))

   


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'cheese': 10 }
  ingredients = { 'milk': 198, 'butter': 52, 'cheese': 10 }
  
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
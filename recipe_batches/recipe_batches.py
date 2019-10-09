#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # recipe_amounts = {}
    least_recipes_by_ingredient = 1000000
    # Loop over recipe ingredients
    for key in recipe:
        if key in ingredients:
            # For each key, check how many recipes can be made by ingredients[key] // recipe[key]
            recipes_with_ingredient = ingredients[key] // recipe[key]
            # If this number is smaller than least_recipes_by_ingredient then update variable
            if recipes_with_ingredient < least_recipes_by_ingredient:
                least_recipes_by_ingredient = recipes_with_ingredient
        else:
            return 0
    return least_recipes_by_ingredient


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

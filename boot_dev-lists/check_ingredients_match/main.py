def check_ingredients_match(recipe, inventory):
    correct = 0.0
    missing_ingredients = []

    for ingredient in recipe:
        if ingredient in inventory:
            correct += 1
        else:
            missing_ingredients.append(ingredient)

    percentage = correct / len(recipe) * 100
    return percentage, missing_ingredients 
    
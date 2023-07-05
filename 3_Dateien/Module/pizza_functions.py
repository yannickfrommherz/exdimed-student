import re
import time

def yn_validator(prompt, yes_regex, no_regex):
    
    reaction_to_invalid_input = "\nBitte antworte entweder mit 'Ja' oder 'Nein'."
    
    while True: 
        
        answer = input(prompt)
    
        if re.fullmatch(yes_regex, answer, re.I):
            return "yes" 
        elif re.fullmatch(no_regex, answer, re.I):
            return "no"
        else:
            time.sleep(1)
            print(reaction_to_invalid_input)

def choose_pizza(first_prompt, alternative_prompt, reaction_to_invalid_input, pizzas):
    
    choice = None
    
    while True:
        
        if not choice: 
            choice = input(first_prompt)
        
        else:
            time.sleep(1)
            print(reaction_to_invalid_input)
            choice = input(alternative_prompt)
            
        for pizza in pizzas.keys():
            if re.fullmatch(pizzas[pizza]["alternative_names"], choice, re.I):
                return pizza

def remove_ingredient(first_prompt, alternative_prompt, reaction_to_invalid_input, ingredients, confirmation, yes_regex, no_regex):
    
    ingredients_lower = [ingredient.lower() for ingredient in ingredients]
    
    while True:
    
        ingredient_to_be_removed = input(first_prompt).lower()

        if ingredient_to_be_removed in ingredients_lower:
            time.sleep(1)
            print(confirmation)
            ingredients_lower.remove(ingredient_to_be_removed)
        else: 
            time.sleep(1)
            print(reaction_to_invalid_input)
        
        remove_another_ingredient = yn_validator(alternative_prompt, yes_regex, no_regex)
        
        if remove_another_ingredient == "no":
            return [ingredient.capitalize() for ingredient in ingredients_lower]
        
def add_ingredient(first_prompt, alternative_prompt, reaction_to_invalid_input, ingredients, extra_ingredients, confirmation, yes_regex, no_regex):
    
    ingredients_lower = [ingredient.lower() for ingredient in ingredients]
    extra_ingredients_lower = [ingredient.lower() for ingredient in extra_ingredients]
    
    while True:
    
        new_ingredient = input(first_prompt).lower()

        if new_ingredient in extra_ingredients_lower and new_ingredient not in ingredients_lower:            
            time.sleep(1)
            print(confirmation)
            ingredients_lower.append(new_ingredient)
        else:
            time.sleep(1)            
            print(reaction_to_invalid_input)
        
        add_another_ingredient = yn_validator(alternative_prompt, yes_regex, no_regex)
        
        if add_another_ingredient == "no":
            return [ingredient.capitalize() for ingredient in ingredients_lower]
        
def request_address(first_prompt, alternative_prompt, reaction_to_invalid_input, w3w_regex):
    
    pizza_destination = None
    
    while True:
    
        if not pizza_destination:
            pizza_destination = input(first_prompt)
        else:
            pizza_destination = input(alternative_prompt)
            
        if re.fullmatch(w3w_regex, pizza_destination, re.I):
            return pizza_destination
        else:
            time.sleep(1)            
            print(reaction_to_invalid_input)
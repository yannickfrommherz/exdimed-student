import re
import time
from pizza_functions import *

#------------> REGEX PATTERNS <------------ 

margherita_regex = r"Margherita"
prosciutto_regex = r"Prosciutto"
vegetariana_regex = r"Vegetariana"

yes_regex = r"Ja"
no_regex = r"Nein"

w3w_regex = r"falschen.fliegen.beliebten"

#------------> AVAILABLE PIZZAS <------------ 

pizzas = {"Margherita": {"alternative_names": margherita_regex, "ingredients": ["Mozzarella", "Tomatensauce", "Oregano"]}, 
          "Prosciutto": {"alternative_names": prosciutto_regex, "ingredients": ["Mozzarella", "Schinken", "Tomatensauce"]}, 
          "Vegetariana": {"alternative_names": vegetariana_regex, "ingredients": ["Mozzarella", "Tomatensauce", "Aubergine", "Zucchini", "Champignons"]}}

extra_ingredients = ["Ananas", "Schinken", "Aubergine", "Mais", "Kirschtomaten", "Parmesan", "Kapern", "Rucola"]

def order_pizza():

    #------------> CHOOSE PIZZA <------------ 
    
    user_name = input("Hallo, ich bin der Pizzabot 🍕🤖\nWie heißt Du?\n")
    
    time.sleep(1)

    first_prompt = "\nSuper " + user_name + ", welche Pizza möchtest Du bestellen?\n"
    reaction_to_invalid_input = "\nDiese Pizza biete ich leider nicht an. 🫤\nBitte wähle zwischen " + ", ".join(pizzas) + ".\n"
    alternative_prompt = "Welche Pizza möchtest Du bestellen, " + user_name + "?\n"

    pizza = choose_pizza(first_prompt, alternative_prompt, reaction_to_invalid_input, pizzas)
    print("\nSuper Wahl! 😋\nDiese Pizza bereite ich mit " + ", ".join(pizzas[pizza]["ingredients"]) + " zu.")

    time.sleep(1)
    
    pizza_ingredients = pizzas[pizza]["ingredients"]

    #------------> CHANGE INGREDIENTS? <------------ 

    prompt = "\nMöchtest Du an den Zutaten etwas ändern?\n"
    change_yn = yn_validator(prompt, yes_regex, no_regex)
    
    if change_yn == "yes":

        #------------> REMOVE INGREDIENTS? <------------ 

        time.sleep(1)
        
        prompt = "\nMöchtest Du eine Zutat entfernen?\n"
        remove_yn = yn_validator(prompt, yes_regex, no_regex)

        if remove_yn == "yes":
            
            time.sleep(1)

            first_prompt = "\nWelche Zutat möchtest Du entfernen?\n"
            alternative_prompt = "\nMöchtest Du eine andere Zutat entfernen?\n"
            reaction_to_invalid_input = "\nDiese Zutat ist nicht auf Deiner Pizza. 🫤"
            confirmation = "\nKlar doch! 👌"

            pizza_ingredients = remove_ingredient(first_prompt, alternative_prompt, reaction_to_invalid_input, pizza_ingredients, confirmation, yes_regex, no_regex)

        #------------> ADD INGREDIENTS? <------------ 
        
        time.sleep(1)

        prompt = "\nMöchtest Du eine Zutat hinzufügen?\n"
        add_yn = yn_validator(prompt, yes_regex, no_regex)

        if add_yn == "yes":
            
            time.sleep(1)

            first_prompt = "\nWelche Zutat möchtest Du hinzufügen?\n"
            alternative_prompt = "\nMöchtest Du eine weitere Zutat hinzufügen?\n"
            reaction_to_invalid_input = "\nDiese Zutat kann ich leider nicht hinzufügen. 🫤\n Sofern nicht bereits auf Deiner Pizza, hast Du die Wahl zwischen " + ", ".join(extra_ingredients) + "."
            confirmation = "\nKlar doch! 👌"

            pizza_ingredients = add_ingredient(first_prompt, alternative_prompt, reaction_to_invalid_input, pizza_ingredients, extra_ingredients, confirmation, yes_regex, no_regex)

    time.sleep(1)

    #------------> VALID ORDER? <------------ 

    if len(pizza_ingredients) < 1:

        print("\nDiese Bestellung ist leider ungültig, da Du sämtliche Zutaten von der Pizza entfernt hast. Bitte bestelle erneut.")

    else:

        print("\nSuper, Du kriegst also eine Pizza " + pizza + " mit " + ", ".join(pizza_ingredients) + ".\n")

        #------------> REQUEST DELIVERY ADDRESS <------------ 
        
        time.sleep(1)
        
        first_prompt = "Wohin darf ich Deine Pizza liefern?\nIch liefere nicht nur zu Dir nach Hause, sondern auch zu Deiner liebsten Bank im Park oder direkt an Dein Strandtuch.\nGib also eine Adresse von www.what3words.com an.\n"
        alternative_prompt = "Diesmal klappt's. Wohin darf ich Deine Pizza liefern?\n"
        reaction_to_invalid_input = "\nSorry, diese Adresse verstehe ich nicht. Ich verstehe aktuell nur 'falschen.fliegen.beliebten'.\n"

        pizza_destination = request_address(first_prompt, alternative_prompt, reaction_to_invalid_input, w3w_regex)
        
        time.sleep(1)
        
        print("\nPerfekt, " + user_name + ". Ich liefere Deine Pizza " + pizza + " an " + pizza_destination + "! 🍕")
        
if __name__ == "__main__":

    order_pizza()